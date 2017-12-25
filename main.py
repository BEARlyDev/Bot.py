# Import class Bot's defenition from bot.py
from bot import Bot

# Make an instance of the bot.
AI = Bot()

# Prompt User for input
while True:
    prompt = AI.user_name + ": "
    que = raw_input(prompt)
    print "AI: "
    if (AI.ask(que.lower())):
        break
