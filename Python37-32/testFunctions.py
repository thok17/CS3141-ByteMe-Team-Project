def changeImage(url):
    global labelImage
    imageAlbum=url_to_image(url)
    labelImage['image']=imageAlbum
    labelImage.image=imageAlbum
    

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	raw_data = urllib.request.urlopen(url).read()
	im = Image.open(io.BytesIO(raw_data))
	im = im.resize((100, 100), Image.ANTIALIAS)
	imageAlbum =ImageTk.PhotoImage(im)
 
	# return the image
	return imageAlbum

def formatMS(number):
    seconds=number/1000
    minutes=int(seconds/60)
    seconds=int(seconds%60)
    formatMS=str(minutes)+" : "+str(seconds)
    return formatMS

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
