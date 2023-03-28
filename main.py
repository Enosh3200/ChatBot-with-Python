#Chatbot with Python



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
   


    Human = input("You: ")
    if Human in chatBot:
        print("ChatBot: ", chatBot[Human])


    else:
        print(random_string())
