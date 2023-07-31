import openai
import os

OPENAI_SECRET_KEY = os.environ.get("OPENAI_SECRET_KEY", "")
CHAT_TEMPERATURE = float(os.environ.get("CHAT_TEMPERATURE", 0))
CHAT_MAX_TOKENS = int(os.environ.get("CHAT_MAX_TOKENS", 50))

openai.api_key = OPENAI_SECRET_KEY

class ImageSize:
    SMALL = "256x256"
    MEDIUM = "512x512"
    LARGE = "1024x1024"

class ImageCost:
    SIZE_TO_COST = {
        ImageSize.SMALL: .016,
        ImageSize.MEDIUM: .018,
        ImageSize.LARGE: .02
    }

    def from_size(size):
        return ImageCost.SIZE_TO_COST[size]

def completion(prompt):
    replies = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=CHAT_TEMPERATURE, max_tokens=CHAT_MAX_TOKENS)
    reply = replies["choices"][0]["text"]

    return reply

def image(prompt, size=ImageSize.MEDIUM):
    response = openai.Image.create(prompt=prompt, size=size)
    print(response)
    image = response["data"][0]["url"]

    return image, ImageCost.from_size(size)