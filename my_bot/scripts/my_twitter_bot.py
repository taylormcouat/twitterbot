import tweepy
import time
import os

FILE_NAME = 'last_seen_id.txt'
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
CONSUMER_KEY   = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')

#Last seen ID: 1331679130874613760

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def compose_tweet():
	names = ["devin", "taylor", "lexis", "poots", "lucky", "kyle", "jake", "amy", "ahmad"]
	last_seen_id = retrieve_last_seen_id(FILE_NAME);
	mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

	for mention in reversed(mentions):
		print("found tweeeeet")
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		count = 0
		for name in names:
			if name in mention.full_text.lower()[9:]:
				count = count + 1
				in_name = name
		if count > 2 :
			status = '@' + mention.user.screen_name + ' HELLO... ' + str(mention.user.screen_name).upper() + ' YOU HAVE INPUTED TOO MANY NAMES. ATTACHED IS SETH MACFARLANE.'
			file = open('seth.jpg', 'rb')
			r1 = api.media_upload(filename = 'seth.jpg', file = file)
		elif count == 0:
			status = '@' + mention.user.screen_name + ' HELLO... ' + str(mention.user.screen_name).upper() + ' YOU HAVE INPUTED AN INVALID NAME. ATTACHED IS LIAM NEESON.'
			file = open('liam.jpg', 'rb')
			r1 = api.media_upload(filename = 'liam.jpg', file = file) 
		else:
			status = '@' + mention.user.screen_name + ' HELLO... ' + str(mention.user.screen_name).upper() + ' REQUEST GRANTED. HERE IS YOUR IMAGE OF ' + in_name.upper() + ' .'
			file = open(in_name + '.jpg', 'rb')
			r1 = api.media_upload(filename = in_name + '.jpg', file = file)
		api.update_status(status=status, in_reply_to_status_id =mention.id, media_ids= [r1.media_id_string])

while True:
	compose_tweet()
	time.sleep(5)





