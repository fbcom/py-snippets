# -*- coding: utf-8 -*-
#
# This is a small helper script that lets you find
# out who is not backfollowing you on twitter.
#
# Known limitations:
#   Irritatingly assumes you only have <200 followers, friends
#
# Install required library:
#   pip install TwitterAPI
#
# Edit settings:
#
CONSUMER_KEY = '
CONSUMER_SECRET = '
ACCESS_TOKEN = '
ACCESS_TOKEN_SECRET = '
#
# Run:
#   python twitter_find_non_backfollowers.py
#

from TwitterAPI import TwitterAPI
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def getFollowersIds(api):
    ret = []
    r = api.request('followers/ids', {'count': 200})
    for item in r.get_iterator():
        ret.append(item)
    return ret


def getFriendsIds(api):
    ret = []
    r = api.request('friends/ids', {'count': 200})
    for item in r.get_iterator():
        ret.append(item)
    return ret


def getUserData(api, user_id):
    r = api.request('users/show', {'user_id': user_id})
    for item in r.get_iterator():
        return item


friend_ids = getFriendsIds(api)
follower_ids = getFollowersIds(api)

# By the Hammer of Grabthar, lets find out who these non-backfollowers are!
users = []
for friend_id in friend_ids:
    if friend_id not in follower_ids:
        user = getUserData(api, friend_id)
        users.append(user)

for user in users:
    print "User @%s (follows %d, has %d followers) is not following you back." % (user['screen_name'], user['friends_count'], user['followers_count'])
