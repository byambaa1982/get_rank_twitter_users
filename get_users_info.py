import tweepy
import pandas as pd
import numpy as np


# ---- you need Twitter Secret Keys in json file and place in the same dir---


with open("twitter_credentials.json", "r") as file:
	creds = json.load(file)
	auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
	auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
	api = tweepy.API(auth, wait_on_rate_limit=True)


def desc_users():
	# Create New empty dictionary 
	users={}
	# Inside it, there are 7 keys: name, screen_name, desctiption and ect
	# All empty lists
	users["ids"] =[]
	users["name"]=[]
	users["screen_name"]=[]
	users["description"]=[]
	users["statuses_count"]=[]
	users["friends_count"]=[]
	users["followers_count"]=[]
	users["account_age"]=[]
	users["average_tweets_per_day"]=[]
	if len(account_list) > 0:
		for target in account_list:
			print("Getting data for " + target)
			users["ids"].append(item.id)
			#  twitter API get_user method used here
			item = api.get_user(target)
			print("name: " + item.name)
			#----- append emtpy list with twitter methods-------------
			users["name"].append(item.name)
			print("screen_name: " + item.screen_name)
				#----- append emtpy list with twitter methods-------------
			users["screen_name"].append(item.screen_name)
			print("description: " + item.description)
				#----- append emtpy list with twitter methods-------------
			users["description"].append(item.description)
			print("statuses_count: " + str(item.statuses_count))
				#----- append emtpy list with twitter methods-------------
			users["statuses_count"].append(item.statuses_count)
			print("friends_count: " + str(item.friends_count))
				#----- append emtpy list with twitter methods-------------
			users["friends_count"].append(item.friends_count)
			print("followers_count: " + str(item.followers_count))
				#----- append emtpy list with twitter methods-------------
			users["followers_count"].append(item.followers_count)
			tweets = item.statuses_count
			account_created_date = item.created_at
			delta = datetime.utcnow() - account_created_date
			account_age_days = delta.days
			users["account_age"].append(account_age_days)
			print("Account age (in days): " + str(account_age_days))
			if account_age_days > 0:
				print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))
				users["average_tweets_per_day"].append(float(tweets)/float(account_age_days))
				
	df=pd.DataFrame(data=users, columns=users.keys())
	return df

def find_inf_rate(username, num_of_followers):
  tweets=tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended', include_rts=False).items(50)
  tweets_list = [([tweet.retweet_count/num_of_followers])*100 for tweet in tweets]
  mysum=sum([tweets_list[i][0] for i in range(0, len(tweets_list))])
  inf_rate=mysum/len(tweets_list)
  return inf_rate
def total_tweets_retweeted(username):
  tweets=tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended', include_rts=False).items(50)
  tweets_list = [tweet.retweet_count for tweet in tweets if tweet.retweet_count!=0]
  return len(tweets_list)

def total_tweets_replied(username):
  tweets=tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended', include_rts=False).items(50)
  tweets_list = [tweet.in_reply_to_status_id for tweet in tweets if type(tweet.in_reply_to_status_id)==int]
  return len(tweets_list)

def find_rt_mention_ratio(rt, mention, total):
  rt_m_ratio=(rt+mention)/total
  return rt_m_ratio

def get_last_tweets_ids(username):
  tweets=tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended', include_rts=False).items(10)
  tweets_list = [tweet.id for tweet in tweets]
  return tweets_list

def get_inique_rtweeters_ids(username):
  tw_list=get_all_tweets_ids(username)
  my_list=[]
  for i in range(len(tw_list)):
    rtweeters_ids=api.retweeters(tw_list[i])
    if len(rtweeters_ids)!=0:
      for id in rtweeters_ids:
        my_list.append(id)
  return len(set(my_list))

def get_number_of_mentions(search_words, date_since):
  new_search = search_words + " -filter:retweets"

  tweets = tweepy.Cursor(api.search, 
                              q=new_search,
                              lang="en",
                              since=date_since).items(2000)

  mentions = [[tweet.id_str] for tweet in tweets]
  return len(mentions)

df=desc_users()

df['number_of_tweets_retweeted']=df.apply(lambda x: total_tweets_retweeted(username = x['screen_name']), axis=1)
df['number_of_tweets_replied']=df.apply(lambda x: total_tweets_replied(username = x['screen_name']), axis=1)
df['rt_mention_ratio']=df.apply(lambda x: find_rt_mention_ratio(rt= x['number_of_tweets_retweeted'], mention=x['number_of_tweets_replied'], total=50), axis=1)
date_since="2021-04-8"
df['number_of_mentions']=df.apply(lambda x: get_number_of_mentions(username = x['screen_name'], date_since=date_since), axis=1)

df.to_excel("sorted_SNP.xlsx")


