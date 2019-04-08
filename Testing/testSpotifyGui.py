import unittest
#import SpotifyGui

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
url=track['item']['album']['images'][0]['url']
trackNumber=track['item']['track_number']
album=track['item']['album']['name']
duration_ms=track['progress_ms']

def formatMS(number):
    seconds=number/1000
    minutes=int(seconds/60)
    seconds=int(seconds%60)
    formatMS=str(minutes)+" : "+str(seconds)
    return formatMS

def changeImage(url):
    global labelImage
    imageAlbum=url_to_image(url)
    labelImage['image']=imageAlbum
    labelImage.image=imageAlbum
    return imageAlbum

def nextTrack():
    nextTrack=spotifyObject.next_track(deviceID)
    track=spotifyObject.current_user_playing_track()
    playback=spotifyObject.current_playback()
    artist=track['item']['artists'][0]['name']
    url=track['item']['album']['images'][0]['url']
    trackNumber=track['item']['track_number']
    album=track['item']['album']['name']
    track=track['item']['name']
    changeImage(url)
    searchResults=spotifyObject.search(artist,1,0,"artist")
    name=searchResults['artists']['items'][0]
    followers=name['followers']['total']
    label_1_song['text']="Song: {}".format(track)
    label_1_artist['text']="Arist: {}".format(artist)
    label_album['text']="Album: {}".format(album)
    label_trackNumber['text']="Track number: {}".format(trackNumber)
    label_followers['text']="Followers: {}".format(followers)
    return track

def muteUnmuteTrack():
    global mute
    global btnMute
    global volume
    volume=devices['devices'][0]['volume_percent']
    if(btnMute.image==mute):
        volume=spotifyObject.volume(0, deviceID)
        btnMute['image']=unmute
        btnMute.image=unmute
    else:
        volume=spotifyObject.volume(volume, deviceID)
        btnMute['image']=mute
        btnMute.image=mute
    return volume


        
def update():
    track=spotifyObject.current_user_playing_track()
    duration_ms=track['progress_ms']
    duration_ms=formatMS(duration_ms)
    lblDuration.configure(text="Duration: "+duration_ms)
    artist=track['item']['artists'][0]['name']
    url=track['item']['album']['images'][0]['url']
    trackNumber=track['item']['track_number']
    album=track['item']['album']['name']
    track=track['item']['name']
    changeImage(url)
    searchResults=spotifyObject.search(artist,1,0,"artist")
    name=searchResults['artists']['items'][0]
    followers=name['followers']['total']
    label_1_song['text']="Song: {}".format(track)
    label_1_artist['text']="Arist: {}".format(artist)
    label_album['text']="Album: {}".format(album)
    label_trackNumber['text']="Track number: {}".format(trackNumber)
    label_followers['text']="Followers: {}".format(followers)
    threading.Timer(0.01, update).start()
    return track

    
    

def previousTrack():
    previousTrack=spotifyObject.previous_track(deviceID)
    track=spotifyObject.current_user_playing_track()
    playback=spotifyObject.current_playback()
    artist=track['item']['artists'][0]['name']
    url=track['item']['album']['images'][0]['url']
    trackNumber=track['item']['track_number']
    album=track['item']['album']['name']
    track=track['item']['name']
    changeImage(url)
    searchResults=spotifyObject.search(artist,1,0,"artist")
    name=searchResults['artists']['items'][0]
    followers=name['followers']['total']
    label_1_song['text']="Song: {}".format(track)
    label_1_artist['text']="Arist: {}".format(artist)
    label_album['text']="Album: {}".format(album)
    label_trackNumber['text']="Track number: {}".format(trackNumber)
    label_followers['text']="Followers: {}".format(followers)
    return previousTrack

#This function will be improved so that I can check if song is currently playing or not
#to update the correct botton 
def pausePlayTrack():
    global playSong
    global pauseSong
    global btnPause
    if (btnPause.image==playSong):
        btnPause['image']=pauseSong
        btnPause.image=pauseSong
        start_playback=spotifyObject.start_playback(deviceID)
    else:
        pause_playback=spotifyObject.pause_playback(deviceID)
        btnPause['image']=playSong
        btnPause.image=playSong
    return btnPause.img
    

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	raw_data = urllib.request.urlopen(url).read()
	im = Image.open(io.BytesIO(raw_data))
	im = im.resize((100, 100), Image.ANTIALIAS)
	imageAlbum =ImageTk.PhotoImage(im)
 
	# return the image
	return imageAlbum


class TestSpotifyGUI(unittest.TestCase):
   def test_formatMS(self):
       result=formatMS(10000)
       self.assertEqual(result,"0 : 10")
       
   def test_nextTrack(self):
       result=nextTrack()
       self.assertEqual(result,spotifyObject.next_track(deviceID))
       
   def test_changeImage(self):
       result=changeImage(url)
       self.assertEqual(result,labelImage)
       
   def test_muteUnmuteTrack(self):
       global mute
       global btnMute
       global volume
       volume=devices['devices'][0]['volume_percent']
       result=muteUnmuteTrack()

       if(btnMute.image==mute):
           self.assertEqual(result,0)
       else:
           self.assertEqual(result,volume)
       
       
   def test_update(self):
       result=update()
       self.assertEqual(result,spotifyObject.current_user_playing_track())
       
   def test_previousTrack(self):
       result=previousTrack()
       self.assertEqual(result,spotifyObject.previous_track(deviceID))
       
   def test_pausePlayTrack()(self):
       global playSong
       global pauseSong
       global btnPause
       
       result=pausePlayTrack()

       if (btnPause.image==playSong):
           self.assertEqual(result,playSong)
       else:
           self.assertEqual(result,pauseSong)

       
if (__name__=='__main__'):
    unittest.main()
        
        
