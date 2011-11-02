import requests
import simplejson
import time
import math
import copy
import os
import apikey
path = '/home/ocoutts/host/get_friends/logs/'
print path

def get_friends(access_token = apikey.APIKEY):
    friends_api_endpoint = "https://graph.facebook.com/me/friends?access_token="+access_token
    r = requests.get(friends_api_endpoint)

    try:
        data = simplejson.loads(r.content)['data']
    except KeyError:
    	print r.content
    	raise Exception("It looks like this is an expired api token")

    friends = {}
    for friend in data:
        friends[friend["id"]]=friend["name"]

    return friends

def store_friend_data(friends):
    f = open(path+"friends.json",'w')
    f.write(simplejson.dumps(friends))
    f.close()

def load_friends():
	f = open(path+"friends.json",'r')
	data = f.read()
	f.close()
	return simplejson.loads(data)

def compare(new_friends):
	old_friends = load_friends()

	events = []

	for friend in old_friends:
		if friend in new_friends:
			del(new_friends[friend])
		else:
			events.append({"name":old_friends[friend],"id":friend, 'status':'lost'})

	for friend in new_friends:
		events.append({"name":new_friends[friend],"id":friend,'status':'added'})

	log(events)


def log(events):
	t = int(math.floor(time.time()))

	f = open(path+"friend_log.json",'r')
	data = f.read()
	f.close()
	try:
		#empty log file case
	    log = simplejson.loads(data)
	except:
		log = []

	if type(log)==str:
     		#empty log file case
		log = []

	for event in events:
		event['time']=t
		log.append(event)

	f = open(path + "friend_log.json",'w')
	f.write(simplejson.dumps(log))
	f.close()

if __name__=="__main__":
	queried_friends = get_friends()
	compare(copy.deepcopy(queried_friends))
	store_friend_data(queried_friends)
