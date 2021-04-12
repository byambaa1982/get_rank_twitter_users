import tweepy
import pandas as pd
import numpy as np

# Influence Score Calculation Function 
def find_inf_rate(username, num_of_followers):
  tweets=tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended', include_rts=False).items(500)
  tweets_list = [([tweet.retweet_count/num_of_followers])*100 for tweet in tweets]
  mysum=sum([tweets_list[i][0] for i in range(0, len(tweets_list))])
  inf_rate=mysum/len(tweets_list)
  return inf_rate

# Add Score into DataFrame 

df=pd.read_csv("all_users_info.csv")
df['influencer_score']=df.apply(lambda x: find_inf_rate(username = x['screen_name'], num_of_followers = x['followers_count']), axis=1)
df2.to_excel("sorted_by_influencer_score.xlsx")