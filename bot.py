import datetime as dt
import random as ra


# Bot Class defenition
class Bot:
    # Constuctor to initialize object of Bot.
    def __init__(self):
        print "\tHey there, this is an AI \n\n\nBefore you start to chat"
        self.user_name = raw_input("can I get your name?\n")

    # Ask Function
    def ask(self, que):
        qu = str(que).split(" ")
        # Give maximum number of fallbacks to greetings, to not miss.
        if que in ["Hello", "hello", "Hi", "hi"]:
            print "Hello there" + self.user_name
        # Let the User decide whether to exit the program.
        elif que in ["exit", "Exit", "X"]:
            yes = raw_input("\n\t\t\tAre you sure?(Y/N).\n")
            if yes.lower() in ["yes", "y"]:
                return(True)

        elif que in ["name", "Name"]:
            print "\n\t\tMy name is V!\n\t\tcreated by Group 8 in python"
        elif qu[0].lower() in ["ask", "quiz"]:
            print trivia()
        elif qu[0].lower() in ["calc", "calculate"]:
            calcu(qu[1])
        elif que in ["joke", "funny"]:
            joke()
        elif que in ["What is the time?", "time", "Time"]:
            show_time()
        else:
            print self.reply(que)
        '''
        Only if the User doen't want to exit should his question go to the AI.
        Pass User's input to the AI and let it respond.
        '''

    def reply(self, que):
        # Open the textfile for read.
        M = open("memory.db", "r")
        # Search through the file until end is reached.
        for line in M.readlines():
            lit = line.split(":")
            if (lit[0].lower() == que.lower()):
                return lit[1]

        else:
            # If reply couldn't find input in textfile close it to reopen!
            M.close()
            # Open memory.db for output, and use append mode.
            M = open("memory.db", "a")
            # Get the ideal output.
            print "I don't know what you mean when you say \'", que, "\', what should I say?\n"
            ideal = raw_input("\tIDEAL REPLY (PLEASE INPUT) : ")
            # Write the ideal output to memory.
            M.write(que + ":" + ideal + "\n")
            return "Done? try exit "

        # Close the file!
        M.close()

    def rename(self, name):
        self.user_name = name


# Joke function by Naveen Subbaram
def joke():
    try:
        f = open("./joke.db", "r")
        lines = f.readlines()
        jo = lines[ra.randrange(len(lines))].split("|")
        print jo[0], "\n", jo[1]
    except IOError:
        print "Non-Existent file"


# Trivia function by Sreelakshmi TS
def trivia():
    try:
        f = open("./trivia.db", "r")
        lines = f.readlines()
        que = lines[ra.randrange(len(lines))].lower().split(":")
        print que[0]  # prints the question
        # Allow user to input answer and compare it to see it contains keyword
        for i in raw_input("A.").lower().split(" "):
            if i in que[1]:
                return "CORRECT ANSWER"
        else:
            return "WRONG ANSWER"
    except IOError:
        print "Non-Existent file"


# By Naveen Subbaram
def show_time():
    now = dt.datetime.now()
    print "Current date and time:", now.strftime("%Y-%m-%d %T")


# Calculate Function by Akhila Asok
def calcu(eq):
    if "+" in eq:
        s = eq.split("+")
        print eq, "is", int(s[0]) + int(s[1])
    elif "-" in eq:
        s = eq.split("-")
        print eq, "is", int(s[0]) - int(s[1])
    elif "*" in eq:
        s = eq.split("*")
        print eq, "is", int(s[0]) * int(s[1])
    elif "/" in eq:
        s = eq.split("/")
        print eq, "is", int(s[0]) / int(s[1])
    else:
        print "I can't calculate that...\n"
