import spotipy
import sys
import json

"""spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + "Rihanna", type='artist')
print (results)"""

import os
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# import the necessary packages
import numpy as np
import urllib.request
import cv2
# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image



#Get the username from terminal.
#username=sys.argv[1]

#userID=84fCxY5cRiWF0WnufNPsGg

#Erase cache and promt for user premission

scope="user-read-private user-read-playback-state user-modify-playback-state"
try:
    token = util.prompt_for_user_token("84fCxY5cRiWF0WnufNPsGg",scope,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')


except:
    os.remove(f".cache-84fCxY5cRiWF0WnufNPsGg")
    token = util.prompt_for_user_token("84fCxY5cRiWF0WnufNPsGg",scope,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')


#create spotify object
spotifyObject=spotipy.Spotify(auth=token)

#get current device:
devices=spotifyObject.devices()
print(json.dumps(devices,sort_keys=True,indent=4))
print()
deviceID=devices['devices'][0]['id']
track=spotifyObject.current_user_playing_track()
print(json.dumps(track,sort_keys=True,indent=4))
print()
playback=spotifyObject.current_playback()
print(json.dumps(playback,sort_keys=True,indent=4))
artist=track['item']['artists'][0]['name']
track=track['item']['name']

if artist!='':
    print("Currently playing: " +artist+"-"+track)


#print(json.dumps(VARIABLE,sort_keys=True,indent=4))
user=spotifyObject.current_user()
print(json.dumps(user,sort_keys=True,indent=4))
displayName=user['display_name']
followers=user['followers']['total']
print("username: "+displayName+"\nnumber of followers: "+str(followers))

while True:
    print()
    print(">>> Welcome to Spotiphy" + displayName)
    print("Search for artist")
    choice=input("Your choice: ")
    if choice=="0":
        print("")
        #search artist
        searchQuery=input("Ok, what's their name?: ")
        #search results
        searchResults=spotifyObject.search(searchQuery,1,0,"artist")
        print(json.dumps(searchResults,sort_keys=True,indent=4))
        #artist details
        artist=searchResults['artists']['items'][0]
        print(json.dumps(artist,sort_keys=True,indent=4))
        print(artist['name'])
        print(str(artist['followers']['total'])+" followers")
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID=artist['id']

        #album details
        trackURIs=[]
        trackArt=[]
        z=0

        #extract album data
        albumResults=spotifyObject.artist_albums(artistID)
        albumResults=albumResults['items']
        for item in albumResults:
            print("Album: "+item['name'])
            albumID=item['id']
            albumArt=item['images'][0]['url']
            trackResults=spotifyObject.album_tracks(albumID)
            trackResults=trackResults['items']
            for item in trackResults:
                print(str(z)+": "+item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()
        #see album art
        while True:
            songSelection=input("Enter song number to see album art and play the song(x to exit)")
            if songSelection=="x":
                break
            trackSelectionList=[]
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID,None,trackSelectionList)
            image = url_to_image(trackArt[int(songSelection)])
            cv2.imshow("Image", image)
            cv2.waitKey(0)
            #webbrowser.open(trackArt[int(songSelection)])
            if songSelection=="1":
                nextTrack=spotifyObject.pause_playback(deviceID)
                trackSelectionList.append
                
                audio=spotifyObject.audio_features(trackURIs)
                print(json.dumps(audio,sort_keys=True,indent=4))
                break
        
   

"""export SPOTIPY_CLIENT_ID='756f6e8b3ffe477ea87a2a53a56bfb6f'
export SPOTIPY_CLIENT_SECRET='37b0f26267004da3bbb636334155aaab'
SPOTIPY_REDIRECT_URI='https://google.com/"""
