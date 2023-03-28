#Chatbot with Python
import random
from datetime import datetime
#saytime = time.ctime()
DateandTime = datetime.now()

chatBot = {
    "hai":"Hello",
    "hey":"Hai",
    "whats up":"I'm good!!!!",
    "what is your name":"My name is Jarvis",
    "how are you":"Somewhere between better and best",
    "how old are you":"Iam Immortal",
    "make me a coffee":"I will make it right away!..",
    "what is the time": DateandTime,
    "what can you do for me":"whatever you command",
    "what is python":"Python is an interpreted, object-oriented,\n high-level programming language with dynamic semantics.",
    "how are you doing":"I'm good, thanks for asking",

}

while True:
    def random_string():
        random_list = [
            "Please try writing something more descriptive.",
            "Oh! It appears you wrote something I don't understand yet",
            "Do you mind trying to rephrase that?",
            "I'm terribly sorry, I didn't quite catch that.",
            "I can't answer that yet, please try asking something else."
        ]

        list_count = len(random_list)
        random_item = random.randrange(list_count)

        return random_list[random_item]


    Human = input("You: ")
    if Human in chatBot:
        print("ChatBot: ", chatBot[Human])


    else:
        print(random_string())
