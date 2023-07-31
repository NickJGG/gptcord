WORDS = ["ability","because","call","down","each","fact","get","having","it","just","keep","life","makes","nation","our","people","quality","realize","so","that","under","very","will","x-ray","you","zone","able","before","can","during","each","failed","gave","if","just","key","like","man","now","over","question","right","still","the","until","visit","want","x-ray","your","zero","about","behind","care","each","fair","general","in","keep","long","near","possible","rise","stop","their","use","very","year","yourselves","above","below","carry","early","fall","give","into","know","look","need","prepare","run","such","then","various","very","yield","yourself","across","benefit","cause","easy","familiar","good","last","loud","none","present","safe","suddenly","there","very","young","absence","better","certain","each","far","govern","latter","love","none","prevent","same","suffer","therefore","view","zero","accept","between","change","either","fast","great","laugh","low","normal","previous","save","suffer","these","violent","access","big","charge","either","fear","greatly","lead","lucky","not","probably","say","sufficient","they","visit","accident","blame","check","either","feed","group","learn","lying","note","problem","school","suggest","think","achieve","blind","choice","either","feel","grow","leave","manage","notice","produce","science","suitable","threat","accuse","block","choose","either"]

class Meta(type):
    def __str__(self):
        return f"**{ self.NAME }** `{ self.COMMAND }` - { self.DESCRIPTION }"

class Activity(metaclass=Meta):
    def __init__(self, bot, message, group=None):
        self.bot = bot
        self.group = group
        self.message = message

    async def play(self):
        pass
