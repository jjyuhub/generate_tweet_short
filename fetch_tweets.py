import requests
import os

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
QUERY = "#AI OR #Tech -is:retweet lang:en"

headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
url = f"https://api.twitter.com/2/tweets/search/recent?query={QUERY}&max_results=3"

response = requests.get(url, headers=headers)
tweets = response.json().get("data", [])

with open("tweets.txt", "w") as f:
    for tweet in tweets:
        f.write(tweet["text"] + "\n")
