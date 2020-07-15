import tweepy
import time

auth = tweepy.OAuthHandler("VC0f2Ygx6TIDHTtAlu0hR3KMU",
                           "Gztnq7DeD7EKxfygbDIOA0XjVBkRPPduQqUdJTFqnLAfRZfE1E")
auth.set_access_token(
    "547241818-q8OgAxh8ZVLAntBEEG5DZcNamxuLErUJVJfbziXB", "sOUgApP4AXQgvM4A1snSoKgchr8Bo3ZIEBk1rngrxDsWg")

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    follower.follow()

search_string = "python"
numbersOfTweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numbersOfTweets)):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
