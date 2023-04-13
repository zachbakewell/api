import tweepy
import keys

client = tweepy.Client(bear_token=keys.bear_token)

response = client.get_user(username='elonmusk')

print(response)

response = client.get_users_followers(id=44196397)

print(response)

a,b,c,d = response

for x in a:
    print(x)

query = 'ADHD at my job -is:retweet -had:media'

response = client.search_recent_tweets(query=query, max_results=100)

print(response)