import spotipy
import sys
import json
import spotipy
"""spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print (results)"""

import os
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

#Get the username from terminal.
#username=sys.argv[1]

#userID=84fCxY5cRiWF0WnufNPsGg

#Erase cache and promt for user premission


token = util.prompt_for_user_token("84fCxY5cRiWF0WnufNPsGg",scope=None,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')



os.remove(f".cache-{84fCxY5cRiWF0WnufNPsGg}")
token = util.prompt_for_user_token(username)


#create spotify object
spotifyObject=spotipy.Spotify(auth=token)

"""export SPOTIPY_CLIENT_ID='756f6e8b3ffe477ea87a2a53a56bfb6f'
export SPOTIPY_CLIENT_SECRET='37b0f26267004da3bbb636334155aaab'
SPOTIPY_REDIRECT_URI='https://google.com/"""

