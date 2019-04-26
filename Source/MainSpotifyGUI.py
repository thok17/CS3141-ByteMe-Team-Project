from tkinter import*
import os
import sys
import subprocess
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import urllib.request
import numpy as np
import cv2
from tkinter import PhotoImage
from PIL import Image
import io
from PIL import ImageTk
import time
import threading
import mysql.connector
from mysql.connector import Error
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox


voteCount=0
groupCount=0
profileCount=0
volume=0
isHost=False
isInGroup=False
connection=""
syncGroup="" #This represent the groupName of the group that usr is currently listening to.
endProgram=False


urlID=input("Type in your Spotify username: ")






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


scope="user-read-private user-read-playback-state user-modify-playback-state"

try:
    token = util.prompt_for_user_token(urlID,scope=scope,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')


except:
    os.remove(f".cache-"+urlID)
    token = util.prompt_for_user_token(urlID,scope=scope,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')


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
searchResults=spotifyObject.search(artist,1,0,"artist")
name=searchResults['artists']['items'][0]
followers=name['followers']['total']




def formatMS(number):
    seconds=number/1000
    minutes=int(seconds/60)
    seconds=int(seconds%60)
    formatMS=str(minutes)+" : "+str(seconds)
    return formatMS

duration_ms=formatMS(duration_ms)
print("Duration: " + str(duration_ms))
track=track['item']['name']


if artist!='':
    print("Currently playing: " +artist+"-"+track)

def nextTrack():
    try:
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
    except:
        premiumMessage()
def muteUnmuteTrack():
    try:
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
    except:
        premiumMessage()

"""def playPauseUpdate():
    track=spotifyObject.current_user_playing_track()
    isPlaying=track['is_playing']
    if (isPlaying):
        btnPause['image']=pauseSong
        btnPause.image=pauseSong
    else:
        btnPause['image']=playSong
        btnPause.image=playSong
    threading.Timer(0.05, playPauseUpdate).start()"""


        
def update():
    global endProgram
    if (endProgram):
        return
    track=spotifyObject.current_user_playing_track()
    isPlaying=track['is_playing']
    if (isPlaying):
        btnPause['image']=pauseSong
        btnPause.image=pauseSong
    else:
        btnPause['image']=playSong
        btnPause.image=playSong
    
    try:
        duration_ms=track['progress_ms']
        duration_ms=formatMS(duration_ms)
        lblDuration.configure(text="Duration: "+duration_ms)
    except:
        lblDuration['text']="Duration: unknown"
       
        
    try:
        artist=track['item']['artists'][0]['name']
        label_1_artist['text']="Arist: {}".format(artist)
    except:
        label_1_artist['text']="Arist: unknown"
    try :
        url=track['item']['album']['images'][0]['url']
        changeImage(url)
    except:
        pImage = Image.open('Default_user_Profile.png')
        pImage = pImage.resize((100, 100), Image.ANTIALIAS)
        imageAlbum =ImageTk.PhotoImage(pImage)
        labelImage['image']=imageAlbum
        labelImage.image=imageAlbum

    try:
        trackNumber=track['item']['track_number']
        album=track['item']['album']['name']
        label_album['text']="Album: {}".format(album)
        label_trackNumber['text']="Track number: {}".format(trackNumber)
    except:
        label_album['text']="Album: unknown"
        label_trackNumber['text']="Track number: unknown"

    isPlaying=track['is_playing']
   
    try:
        track=track['item']['name']
        label_1_song['text']="Song: {}".format(track)
    except:
        label_1_song['text']="Song: unknown"
    try:
        searchResults=spotifyObject.search(artist,1,0,"artist")
        name=searchResults['artists']['items'][0]
        followers=name['followers']['total']
        label_followers['text']="Followers: {}".format(followers)
    except:
        label_followers['text']="Followers: unknown"
    threading.Timer(0.01, update).start()
    
    
    
def previousTrack():
    try:
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
    except:
        premiumMessage()

def pausePlayTrack():
    try:
        global playSong
        global pauseSong
        global btnPause    
        if (btnPause.image==playSong):
            #btnPause['image']=pauseSong
            #btnPause.image=pauseSong
            start_playback=spotifyObject.start_playback(deviceID)
        else:
            pause_playback=spotifyObject.pause_playback(deviceID)
            #btnPause['image']=playSong
            #btnPause.image=playSong
    except:
        premiumMessage()
    

def apps():
    mainFrameVote.place_forget()
    mainFrameGroup.place_forget()
    mainFrameProfile.place_forget()
    mainFrameApp.place(x=0,y=25,relheight="1",relwidth="0.8962")
    middleFrame.pack()
    rps=PhotoImage(file="rps.png")
    botton_1=Button(middleFrame,image=rps,compound=TOP, command=rps1)
    botton_1.image=rps
    botton_1.grid(row=0,padx=10,pady=10)
    botton_2=Button(middleFrame,text="app_2",width=10, bg="white")
    botton_2.grid(row=0,column=1,padx=10,pady=10)
    botton_3=Button(middleFrame,text="app_3",width=10, bg="white")
    botton_3.grid(row=1,padx=10,pady=10)
    botton_4=Button(middleFrame,text="app_4",width=10, bg="white")
    botton_4.grid(row=1,column=1,padx=10,pady=10)

def rps1():
    subprocess.Popen('python RPS_GUI.py')
    

def findArtistAlbums(artist,txt,btnFrame,playFrame,entry):
    try:
        searchResults=spotifyObject.search(artist,1,0,"artist")
        artist=searchResults['artists']['items'][0]
        url=artist['images'][0]['url']
        artistID=artist['id']

            #album details
        global trackURIs
        global trackArt
        global z
        trackURIs=[]
        trackArt=[]
        z=0

            #extract album data
        albumResults=spotifyObject.artist_albums(artistID)
        albumResults=albumResults['items']
        text=""
        for item in albumResults:
            text+="\nAlbum: "+item['name']+"\n"
            #text['font']=('consolas', '9')
            albumID=item['id']
            albumArt=item['images'][0]['url']
            trackResults=spotifyObject.album_tracks(albumID)
            trackResults=trackResults['items']
            for item in trackResults:
                text+=str(z)+": "+item['name']+"\n"
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            #see album art
        txt.delete('1.0',END)
        txt.insert(INSERT,text)

        btnShowPic=Button(btnFrame,text="picture",width=7,command=lambda:openNewWindow(url))
        btnShowPic.grid(row=0,column=3)
        playFrame.grid()
        entry.delete('0',END)
        entry.insert('0',"")
    except:
        messagebox.showinfo('Attention', "Error. Artist not found. Please try again.")


def playNumberSong(songNumber,entry):
    global trackURIs
    global trackArt
    global z
    try:
        trackSelectionList=[]
        trackSelectionList.append(trackURIs[int(songNumber)])
        spotifyObject.start_playback(deviceID,None,trackSelectionList)
    except: messagebox.showinfo("Attention", "Was not able to play chosen song number. Please try again")
             
    entry.delete('0',END)
    entry.insert('0',"")
    
def openNewWindow(url): #Open window to display picture of artist. 
    newwin = Toplevel(root)
    changeImage(url)
    raw_data = urllib.request.urlopen(url).read()
    im = Image.open(io.BytesIO(raw_data))
    im = im.resize((300, 320), Image.ANTIALIAS)
    imageArtist =ImageTk.PhotoImage(im)
    lblImg=Label(newwin,image=imageArtist)
    lblImg.image=imageArtist
    lblImg.pack()
    
    
#albumDetails
trackURIs=[]
trackArt=[]
z=0

def songs():
    global voteCount
    mainFrameGroup.place_forget()
    mainFrameApp.place_forget()
    mainFrameProfile.place_forget()
    mainFrameVote.place(x=0,y=25,relheight="1",relwidth="0.8962")
    if (voteCount==0):
        scrollFrame=Frame(mainFrameVote,bg="limegreen")
        yscrollbar = Scrollbar(scrollFrame)
        yscrollbar.pack(side = RIGHT, fill = Y)
        xscrollbar = Scrollbar(scrollFrame,orient='horizontal')
        text = Text(scrollFrame, width = 48, height = 11, wrap = NONE,
                    yscrollcommand = yscrollbar.set,xscrollcommand=xscrollbar.set)
        text['font']=('consolas', '9')
        text.pack()
        xscrollbar.pack(side = BOTTOM, fill = X,anchor='w')
        yscrollbar.config(command = text.yview)
        xscrollbar.config(command = text.xview)
        """txt = ScrolledText(mainFrameVote, width=48,height=13)
        txt['font'] = ('consolas', '9')"""
        searchFrame=Frame(mainFrameVote,bg="limegreen")
        e = Entry(searchFrame, width=15)
        lblArtist=Label(searchFrame,text="Please enter an artist:",bg="limegreen")
        lblArtist.grid(row=0,column=0)
        e.grid(row=0,column=1)
        #txt.grid(row=1,columnspan=4,padx=1)
        btnAlbum=Button(searchFrame,text="search",width=7,command=lambda:findArtistAlbums(e.get(),text,searchFrame,playFrame,e))
        btnAlbum.grid(row=0,column=2)
        playFrame=Frame(mainFrameVote,bg="limegreen")
        lblSong=Label(playFrame,text="Please enter a number to play a song:",bg="limegreen")
        lblSong.grid(row=0,ipadx=5)
        e2 = Entry(playFrame, width=5)
        e2.grid(row=0,column=1,ipadx=5)
        btnAlbum=Button(playFrame,text="play",width=7,command=lambda:playNumberSong(e2.get(),e2))
        btnAlbum.grid(row=0,column=2,padx=5,pady=2)
        searchFrame.grid()
        scrollFrame.grid()
    voteCount+=1

def profiles():
    print("is at method profiles")
    global profileCount
    mainFrameGroup.place_forget()
    mainFrameApp.place_forget()
    mainFrameVote.place_forget()
    mainFrameProfile.place(x=0,y=25,relheight="1",relwidth="0.8962")



    #Get profile information. Might have this in a try/catch clause. 
    user=spotifyObject.current_user()
    print(json.dumps(user,sort_keys=True,indent=4))
    displayName=user['display_name']
    followers=user['followers']['total']
    print("username: "+displayName+"\nnumber of followers: "+str(followers))
    try:
        url_image = user['images'][0]['url']
        raw_image = urllib.request.urlopen(url_image).read()
        pImage = Image.open(io.BytesIO(raw_image))
        pImage = pImage.resize((100, 100), Image.ANTIALIAS)
        imageProfile =ImageTk.PhotoImage(pImage)
        lblProfileImage=Label(mainFrameProfile,image=imageProfile,bg="#262626", fg="white", anchor=E,font=("Helvetica",12,"bold", "italic"))
        lblProfileImage.image=imageProfile
    except:
        pImage = Image.open('Default_user_Profile.png')
        pImage = pImage.resize((100, 100), Image.ANTIALIAS)
        imageProfile =ImageTk.PhotoImage(pImage)
        lblProfileImage=Label(mainFrameProfile,image=imageProfile,bg="#262626", fg="white", anchor=E,font=("Helvetica",12,"bold", "italic"))
        lblProfileImage.image=imageProfile
        
    playlists = spotifyObject.user_playlists(user['id'])
    for playlist in playlists['items']:
            if (playlist['owner']['id'] == user['id']):
                print()
                print(playlist['name'])

    if (profileCount==0):
        lblProfileImage.pack()
        lblName=Label(mainFrameProfile,text="Username: "+displayName,bg="black", fg="white",font=("Helvetica",12,"bold", "italic"))
        lblName.pack()
        lblFollowers=Label(mainFrameProfile,text="Number of followers: "+str(followers),bg="black", fg="white",font=("Helvetica",12,"bold", "italic"))
        lblFollowers.pack()
    profileCount+=1


#Getting user id
user=spotifyObject.current_user()
usrID="Lena"



#Finds all active Groups that user is a part of
def findActiveGroups(usrID,txt):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from isPartOf natural join GroupPlaying where username="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        text=""
        try:
            for row in records:
                text+=(row[0]+"\n")
                
        except:
            print("No active groups")
        finally:
            txt.delete('1.0',END)
            txt.insert(INSERT,text)

#Finds all groups where user i host. 
def findMyGroups(usrID,txt):
    if (connection.is_connected()):
        sqlQuery = "select group_name from Groups where host_name="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        text=""
        try:
            for row in records:
                text+=(row[0]+"\n")
        except:
            messagebox.showinfo('Attention', "There's no active groups")
        finally:
            txt.delete('1.0',END)
            txt.insert(INSERT,text)




#Check if group name is in Group table
def checkGroup(groupName):
    if (connection.is_connected()):
        sqlQuery = "select group_name from Groups where group_name="+"'"+groupName+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==groupName
            return True
        except:
            return False

def checkGroupPlaying(groupName):
    if (connection.is_connected()):
        sqlQuery = "select group_name from GroupPlaying where group_name="+"'"+groupName+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==groupName
            return True
        except:
            return False
    else:
        massegebox.showinfo('Attention', 'Lost connection to server')


#Check if user is already a part of the group:
def checkJoin(groupName):
    if (connection.is_connected()):
        sqlQuery = "select username from isPartOf where group_name="+"'"+groupName+"' and username="+"'"+usrID+"';"
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            for row in records:
                if row[0]==usrID:
                    return True #User is already part of the group
                else:
                    return False #User is not part of the group
        except:
            return False #User is not part of group
           
    
    
    

#Check if user is in User table, if not it adds the user to User table
def checkUser(usrID):
    global connection
    if (connection.is_connected()):
        print(usrID)
        sqlQuery = "select username from User where username="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            print(records[0][0])
            records[0][0]==usrID
            cursor.close()
            return
        except:
            ##sqlQuery = "insert into User values("+"'"+usrID+"'"+");"
            ##print("user created")
            cursor = connection.cursor()
            args=(usrID)
            cursor.callproc('addUser',args=(usrID,))
            connection.commit()
            cursor.close()
            
            
    else:
        connect()
        checkUser(usrID)

#Creating a new group. User is automatically the host
def createGroup(groupName,txtMyGroup,entry):
    global connection
    connect()
    print(usrID)
    checkUser(usrID)
    #Check to see that there's not already a group with the same name
    if (not checkGroup(groupName)): 
            cursor = connection.cursor()
            cursor.callproc('addGroup',args=(groupName,usrID,1))
            cursor.callproc('addPart',args=(usrID,groupName,1))
            entry.delete('0',END)
            entry.insert('0',"")
            cursor.close()
            connection.commit()
            findMyGroups(usrID,txtMyGroup)
            
            

    else:
         messagebox.shoinfo("Attention", "GroupName already exist, so group can't be created with this name.")
  
#Takes in txt and labels to update labels and text in the Group room.
def joinGroup(groupName,txtActiveGroups,entry):
    global connection
    connect()
    checkUser(usrID)
    entry.delete('0',END)
    entry.insert('0',"")
    #Check to see that there exist a group with with name 'groupName'
    if(checkGroup(groupName)):
        if(not checkJoin(groupName)):
            cursor = connection.cursor()
            cursor.callproc('updateGroupNumber',args=(groupName,))
            cursor.callproc('addIsPartOf',args=(usrID,groupName,0))
            connection.commit()
            cursor.close()
            messagebox.showinfo('Attention','You have now joined the group '+groupName)
            
        listenToGroup(groupName,usrID,txtActiveGroups)
        
    else:
         messagebox.showinfo('Attention',"There's no group named "+groupName)
         return
    #Refresh thel list of active and inactive groups in the GUI 
  
#Check if user is host
def checkHost(groupName):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from Groups where group_name="+"'"+groupName+"' and host_name="+"'"+usrID+"';"
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==groupName #This means the user is host
            cursor.close()
            print("The user is Host")
            return True
        except:
            cursor.close()
            return False
            print("The user is not Host")
            
   
def syncToGroup():
    if isHost==(''):
        return
    if isHost==(True):
        push()
    else:
        pull()
        
def push():
    global isHost
    global syncGroup
    if(isHost!=True):
        return
    try:
        if connection.is_connected():
            print("pushing")
            track=spotifyObject.current_user_playing_track()
            uri=track['item']['uri']
            durationMS=str(track['progress_ms'])
            isPlaying=track['is_playing']
            cursor = connection.cursor()
            cursor.callproc('updateGroupPlaying',args=(syncGroup,uri,durationMS,isPlaying))
            cursor.close()
            connection.commit()
            threading.Timer(5.0, push).start()
    except Error as e:
        print("her er feilen")
        messagebox.showinfo('attention',"error while connecting to MySQL")

def pull():
    global isHost
    global syncGroup
    if (isHost!=False):
        thredning.cancel()
        return
    connect()
    try:
        if connection.is_connected():
            print("pulling")
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            sqlQuery1 = "select track_uri from GroupPlaying where group_name='"+syncGroup+"';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery1)
            records = cursor.fetchall()
            track_uri=""
            try:
                records[0][0]
                for row in records:
                    track_uri=str(row[0])
            except:
                messagebox.showinfo('attention',"Can't listen to this group anymore, because host has left!")
                return 
            sqlQuery2 = "select position from GroupPlaying where group_name='"+syncGroup+"';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2)
            records = cursor.fetchall()
            for row in records:
                position=row[0]
            sqlQuery2 = "select isPaused from GroupPlaying where group_name='"+syncGroup+"';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2)
            records = cursor.fetchall()
            for row in records:
                isPaused=row[0]
            track=spotifyObject.current_user_playing_track()
            uri=track['item']['uri']
            durationMS=str(track['progress_ms'])
            isPlaying=track['is_playing']
            if (isPaused==0 and isPlaying==True): #If the song is playing, then pause the song
                spotifyObject.pause_playback(deviceID)
                print("1")
            elif (isPaused==1 and isPlaying==False):
                trackList=[]
                trackList.append(track_uri)
                spotifyObject.start_playback(deviceID,None,trackList)
                spotifyObject.seek_track(int(position), deviceID)
                print("2")

            elif (isPaused==1 and not (track_uri==uri and -10000<int(position)-int(durationMS)<10000)):
                  trackList=[]
                  trackList.append(track_uri)
                  spotifyObject.start_playback(deviceID,None,trackList)
                  spotifyObject.seek_track(int(position), deviceID)
                  print("3")
            
            disconnect()
            threading.Timer(5.00, pull).start()
            
    except Error as e:
        messagebox.showinfo('Attention',"error while connecting to MySQL")

    


#Check if group is avtive, then listens to the group       
def listenToGroup(groupName,usrID,txtActiveGroups):
    global lblListenGroup
    global syncGroup
    global isHost
    if (isActive(syncGroup) and checkHost(groupName)): #If host alrady pulls information to user
        connect()
        cursor = connection.cursor()
        cursor.callproc('deleteGroupPlaying',args=(syncGroup,))
        cursor.close()
        connection.commit()
        isHost=""
        messagebox.showinfo('Attention',"You you just left group "+syncGroup)
        
    
    if (isActive(groupName) or checkHost(groupName)): #Either the group is active, or the user is host and can make the group active
        isHost=checkHost(groupName)
        syncGroup=groupName
        if (isHost): ##Need to have this code here even though it's in the pull function, because of the finActiveGroups needs to be updated only once. 
            try:
                track=spotifyObject.current_user_playing_track()
                uri=track['item']['uri']
                durationMS=str(track['progress_ms'])
                isPlaying=track['is_playing']
                cursor = connection.cursor()
                cursor.callproc('addGroupPlaying',args=(groupName,uri,durationMS,isPlaying))
                cursor.close()
                connection.commit()
            except Error as e:
                    messagebox.showinfo('attention',"error while connecting to MySQL")
        findActiveGroups(usrID,txtActiveGroups)
        syncToGroup() ##This function needs to check the isHost variable and push/pull accordingly
        lblListenGroup['text']="You're now listening to group "+groupName
    else:
        messagebox.showinfo('Attention',"You can't listen to the group "+groupName+",because it's inactive")


#Check if the host is pushing to the GroupPlaying table, if not give a messege that the host is inactive and that the user can't listen to this group
def isActive(groupName):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from GroupPlaying where group_name="+"'"+groupName+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==groupName #This means the group is active
            cursor.close()
            return True
        except:
            cursor.close()
            return False
            
    

def connect():
    global connection
    global cursor
    try:
        connection = mysql.connector.connect(host='classdb.it.mtu.edu',
                                             port='3307',
                                             database='byteme',
                                             user='byteme_rw',
                                             password='password')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)

            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print ("you're connected to - ", record)
            cursor.close()
            connection.commit()
           

    except Exception as e:
        messagebox.showinfo("Attention","error while connecting to MySQL")





    
def disconnect():
    global connection
    if(connection.is_connected()):
        connection.close()


def showGroup(lblListenGroup):
    global syncGroup
    if (syncGroup==""):
            lblListenGroup=Label(mainFrameGroup,text="You are not listening to any groups",bg="black", fg="white", font=("Helvetica",12,"bold"))
            lblListenGroup.grid(row=0,columnspan=2,padx=80,pady=5)
            
    else:
            lblListenGroup=Label(mainFrameGroup,text="You are listening to group "+syncGroup,bg="black", fg="white", font=("Helvetica",12,"bold"))
            lblListenGroup.grid(row=0,columnspan=2)
    


def groups():
    global lblListenGroup
    global groupCount
    global syncGroup

    mainFrameVote.place_forget()
    mainFrameApp.place_forget()
    mainFrameProfile.place_forget()
    mainFrameGroup.place(x=0,y=25,relheight="1",relwidth="0.8962")
    
    if (groupCount==0):
        if (syncGroup==""):
            lblListenGroup=Label(mainFrameGroup,text="Listening to no groups",bg="black", fg="white", font=("Helvetica",10,"bold"),width=45)
            lblListenGroup.grid(row=0,column=0,columnspan=2,sticky=W)
        else:
            lblListenGroup=Label(mainFrameGroup,text="Listening to group "+syncGroup,bg="black", fg="white", font=("Helvetica",10,"bold"))
            lblListenGroup.grid(row=0,columnspan=2)

        lblActiveGroup=Label(mainFrameGroup,text="My active groups: ",bg="black", fg="white", font=("Helvetica",10,"bold"))
        lblActiveGroup.grid(row=1, column=0,ipadx=5,ipady=5)

        lblMyGroup=Label(mainFrameGroup,text="My own groups: ",bg="black", fg="white", font=("Helvetica",10,"bold"))
        lblMyGroup.grid(row=1,column=1,ipady=5,sticky=W)

        txt = ScrolledText(mainFrameGroup, width=10,height=3)
        txt['font'] = ('consolas', '9')
        txt.grid(row=2,column=0)
        findActiveGroups(usrID,txt)

        txt2 = ScrolledText(mainFrameGroup, width=10,height=3)
        txt2['font'] = ('consolas', '9')
        txt2.grid(row=2,column=1,sticky=W)
        findMyGroups(usrID,txt2)
        
        lbljoinGroup=Label(mainFrameGroup,text="Join group: ",bg="black", fg="white", font=("Helvetica",8,"bold"))
        lbljoinGroup.grid(row=3)
        e = Entry(mainFrameGroup, width=15)
        e.grid()
        btnJoin=Button(mainFrameGroup,text="join",command=lambda:joinGroup(e.get(),txt,e))
        btnJoin.grid()
        lblCreateGroup=Label(mainFrameGroup,text="Create group : ",bg="black", fg="white", font=("Helvetica",8,"bold"))
        lblCreateGroup.grid(row=3,column=1,sticky=W,ipadx=10)
        e2 = Entry(mainFrameGroup, width=15)
        e2.grid(row=4,column=1,sticky=W)
        btnCreate=Button(mainFrameGroup,text="create",command=lambda:createGroup(e2.get(),txt2,e2))
        btnCreate.grid(row=5,column=1,sticky=W,padx=25)
        #lblListenGroup=Label(mainFrameGroup,text="You are not listening to any groups",bg="green")
        #lblListenGroup.grid(row=0,columnspan=2,padx=80,pady=5)
        
        


    groupCount+=1

def backToMusic():
    mainFrameApp.place_forget()
    mainFrameVote.place_forget()
    mainFrameProfile.place_forget()
    mainFrameGroup.place_forget()

def premiumMessage():
    messagebox.showinfo('Attention', "You must be a premium user to utilize this action.")
    
    
root=Tk()

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

#positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
#positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
positionRight = int(root.winfo_screenwidth()/2)
positionDown = int(root.winfo_screenheight()/2)
root.configure(background="black")
root.geometry("400x260+{}+{}".format(positionRight, positionDown))
root.maxsize(400,260)
root.title('Spotify sync')




aboveFrame = Frame(root,bg="limegreen")
aboveFrame.pack(side=TOP,fill=X)
profile=PhotoImage(file="profileIcon.png")
btnProfile=Button(aboveFrame,image=profile,fg="black", bg="limegreen",command=profiles)
lblProfile=Label(aboveFrame,text="Spotify Sync",fg="black",bg="limegreen",font=("Helvetica",14,"bold") )
btnProfile.pack(side=RIGHT,ipadx=5)
lblProfile.pack()

"""menubar = Menu(btnProfile)
setting = Menu(menubar, tearoff=0)
setting.add_command(label="something")
setting.add_command(label="something")
setting.add_separator()
setting.add_command(label="Log out", command=root.quit)
menubar.add_cascade(label="Settings", menu=setting)
# display the menu
root.config(menu=menubar)"""

#label.grid(ipadx=105,ipady=2,sticky=N+W)
#btnSettings.grid(row=0,column=2,sticky=E)

bottomLeftFrame=Frame(root,bg="black")
menyFrame=Frame(root,bg="limegreen")
menyFrame.pack(side=RIGHT,fill=Y)
bottomLeftFrame.pack(fill=X)
bottomRightFrame=Frame(root,bg="#262626")
bottomRightFrame.pack(fill=X)

#Frames for our app-layout
mainFrameApp=Frame(root,bg="black")
middleFrame=Frame(mainFrameApp,bg="black")

#Frame for our vote-layout
mainFrameVote=Frame(root,bg="limegreen")

#Frame for our group-layout
mainFrameGroup=Frame(root,bg="black")

#Frame for our profile-layout
mainFrameProfile=Frame(root,bg="black")



music=PhotoImage(file="musicIcon.png")
musicSmall=PhotoImage(file="musicSmallIcon.png")
mute=PhotoImage(file="unmute.png")
unmute=PhotoImage(file="mute.png")
search=PhotoImage(file="searchIcon.png")
app=PhotoImage(file="appIcon.png")
nextSong=PhotoImage(file="nextIcon.png")
playSong=PhotoImage(file="playIcon.png")
pSong=PhotoImage(file="pIcon.png")
pauseSong=PhotoImage(file="pauseIcon.png")
group=PhotoImage(file="groupIcon.png")
btnMusic=Button(menyFrame,text="music",image=musicSmall,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="limegreen", command=backToMusic)
btnMusic.grid()
btnSong=Button(menyFrame,text="song", image=search,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="limegreen",command=songs)
btnSong.grid()
btnApp=Button(menyFrame,text="app", image=app,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="limegreen",command=apps)
btnApp.grid()
btnGroup=Button(menyFrame,text="group", image=group,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="limegreen",command=groups)
btnGroup.grid()


#label_1=Label(bottomLeftFrame,image=music,bg="white",anchor=W, fg="white")
labelCurrentlyPlaying=Label(bottomLeftFrame,text="Currently playing: ",bg="black",fg="lightgray",font=("Helvetica",12,"bold"),anchor=W)
label_1_song=Label(bottomLeftFrame,text="Song: "+ track+"",bg="black",fg="aqua",anchor=W,width=30, font=("Helvetica", 10, "bold"))
label_1_artist=Label(bottomLeftFrame,text="Artist: "+artist+"",bg="black",fg="lightgray",width=30,anchor=W)
label_album=Label(bottomLeftFrame,text="Album: "+ album+"",bg="black",fg="lightgray",anchor=W,width=30)
label_trackNumber=Label(bottomLeftFrame,text="Track number: "+ str(trackNumber)+"",bg="black",fg="lightgray",anchor=W,width=30)
lblDuration=Label(bottomLeftFrame,text="Duration: "+ str(duration_ms)+"",bg="black",fg="lightgray",anchor=W,width=30)
label_followers=Label(bottomLeftFrame,text="Followers: "+ str(followers)+"",bg="black",fg="lightgray",anchor=W,width=30)

#label_1_duration=Label(bottomLeftFrame,text="Duration: mm:ss",bg="white",fg="black",width=35)

label_mute=Label(bottomLeftFrame,image=mute,bg="white")

#Converting url to image
raw_data = urllib.request.urlopen(url).read()
im = Image.open(io.BytesIO(raw_data))
im = im.resize((100, 100), Image.ANTIALIAS)
imageAlbum =ImageTk.PhotoImage(im)
labelImage=Label(bottomRightFrame,image=imageAlbum,bg="#262626", anchor=E,font=("Helvetica",12,"bold", "italic"))

label_2_song=Label(bottomRightFrame,text="Song: X",bg="black",fg="white",width=30)
label_2_artist=Label(bottomRightFrame,text="Artist: X",bg="black",fg="white",width=5)
label_2_change=Label(bottomRightFrame,text="Yes, I want to change to this song song",bg="black",fg="white",width=35)
btnNext=Button(bottomRightFrame,image=nextSong,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="white", command=nextTrack)
btnP=Button(bottomRightFrame,image=pSong,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="white", command=previousTrack)


btnPause=Button(bottomRightFrame,image=playSong,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="white", command=pausePlayTrack)
btnPause.image=playSong
#Check that the correct play/pause image is displaying
#playPauseUpdate()
btnMute=Button(bottomRightFrame,image=mute,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="white", command=muteUnmuteTrack)
btnMute.image=mute
#btnPlay=Button(bottomLeftFrame,image=playSong,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="white", command=playTrack)


cYes=Checkbutton(bottomRightFrame)
cNo=Checkbutton(bottomRightFrame)

labelCurrentlyPlaying.grid(row=0)
label_1_song.grid(row=1)
label_1_artist.grid(row=2)
label_album.grid(row=3)
label_trackNumber.grid(row=3,column=1)
lblDuration.grid(row=4)
label_followers.grid(row=2,column=1)
#label_1.grid(row=0,column=1,ipadx=2)
btnNext.grid(row=1,column=2,padx=10)
btnPause.grid(row=1,column=1,padx=10)
btnP.grid(row=1,column=0,padx=10)
#label_1_duration.grid(row=3,ipadx=5)
btnMute.grid(row=2,column=1,sticky="w",padx=11)
#label_1.grid(row=0,ipadx=5)
labelImage.grid(row=0,column=8,rowspan=3,ipady=5,padx=45)
#label_2_song.grid()
#label_2_artist.grid()
#label_2_change.grid()
#cYes.grid(row=3,column=1,columnspan=1)
#update()


##Accessing the database
track=spotifyObject.current_user_playing_track()
uri=track['item']['uri']
durationMS=str(track['progress_ms'])
isPlaying=track['is_playing']



try:
        connection = mysql.connector.connect(host='classdb.it.mtu.edu',
                                             port='3307',
                                             database='byteme',
                                             user='byteme_rw',
                                             password='password')
        """if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)

            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print ("you're connected to - ", record)


            sql_select_Query = "select host_name from Groups where group_name='byteme';"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            for row in records:
                name=row[0]
                
                
        if (name=="mr.vollset"):
            sqlQuery1="update GroupPlaying set track_uri="+"'"+uri+"'"+" where group_name='byteme';"
            sqlQuery2="update GroupPlaying set position="+durationMS+" where group_name='byteme';"

            cursor.execute(sqlQuery1)
            cursor.execute(sqlQuery2)
            record=cursor.fetchone()
            cursor = connection.cursor()
            cursor.callproc('updateGroupPlaying',args=('byteme',uri,durationMS,isPlaying))
            cursor.close()
            connection.commit()  
            print(record)
            connection.commit()"""
           
            
except Error as e:
        print ("error while connecting to MySQL", e)




finally:

    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


#readDbVersion()



def onClosing():
    global isHost
    global syncGroup
    global endProgram
    global cursor
    msg=messagebox.askokcancel("Quit", "Do you want to quit?")
    if(msg):
        if (isHost==True):
            connect()
            cursor = connection.cursor()
            cursor.callproc('deleteGroupPlaying',args=(syncGroup,))
            cursor.close()
            connection.commit()
            connection.close()
        endProgram=True
        isHost=""
        try:
            os.remove(f".cache-"+urlID)
        except:
            print()
        root.quit()
        root.destroy()
    
    

root.protocol("WM_DELETE_WINDOW", onClosing)


print("End of a Python Database Programming Exercise\n\n")



update()
root.mainloop()
