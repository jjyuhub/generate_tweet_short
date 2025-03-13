import random

with open("tweets.txt", "r") as f:
    tweets = f.readlines()

if not tweets:
    script = "Welcome to today's AI news update! Stay tuned for more tech insights."
else:
    script = random.choice(tweets).strip()

script = f"Here's something interesting: {script}. Stay ahead with AI news."

with open("script.txt", "w") as f:
    f.write(script)
