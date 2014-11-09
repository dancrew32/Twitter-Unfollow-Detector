import os

# https://apps.twitter.com/
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
CACHE_FILE = os.path.join(CURRENT_PATH, '.follower_cache.json')

EMAIL_FROM = 'bot@server.com'
EMAIL_TO = 'you@you.com'
