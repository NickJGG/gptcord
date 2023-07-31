FROM python:3.8-slim

WORKDIR /usr/src/gptcord

VOLUME ./:/usr/src/gptcord

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "app.py"]