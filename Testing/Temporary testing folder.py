import unittest
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


#import SpotifyGui

urle=input("enter ID: ")

scope="user-read-private user-read-playback-state user-modify-playback-state"
try:
    token = util.prompt_for_user_token(urle,scope=scope,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')


except:
    os.remove(f".cache-84fCxY5cRiWF0WnufNPsGg")
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

    return nextTrack

def previousTrack():
    previousTrack=spotifyObject.previous_track(deviceID)
    track=spotifyObject.current_user_playing_track()
    playback=spotifyObject.current_playback()
    artist=track['item']['artists'][0]['name']
    url=track['item']['album']['images'][0]['url']
    trackNumber=track['item']['track_number']
    album=track['item']['album']['name']
    track=track['item']['name']

    return previousTrack

#Finds all active Groups that user is a part of
def findActiveGroups(usrID):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from isPartOf natural join GroupPlaying where username="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        text=""
        try:
            for row in records:
                text=(row[0]+"\n")
                
        except:
            print("No active groups")

        disconnect()
        
    return text

#Finds all groups where user i host. 
def findMyGroups(usrID):
    connect()
    if (connection.is_connected()):
        sqlQuery = "select group_name from Groups where host_name="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        text=""
        try:
            for row in records:
                text=(row[0]+"\n")
        except:
            print("No active groups")
        disconnect()
    return  text



#Check if group name is in Group table
def checkGroup(groupName):
    connect()
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
        disconnect()


#Check if user is in User table, if not it adds the user to User table
def checkUser(usrID):
    global connection
    connect()
    if (connection.is_connected()):
        sqlQuery = "select username from User where username="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
            records[0][0]==usrID
            print("already a user!")
            cursor.close()

            return True

        except:
            ##sqlQuery = "insert into User values("+"'"+usrID+"'"+");"
            ##print("user created")

            return False

        disconnect()
            
    else:
        connect()
        checkUser(usrID)
    return False



#Check if user is host
def checkHost(groupName, usrID):
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
            disconnect()
            return True
        except:
            cursor.close()
            disconnect()
            return False
            print("The user is not Host")
        return False
        

def connect():
    global connection
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
           

    except Exception as e:
        print ("error while connecting to MySQL", e)





    
def disconnect():
    global connection
    if(connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")



class TestSpotifyGUI(unittest.TestCase):
   def test_formatMS(self):
       result=formatMS(10000)
       self.assertEqual(result,"0 : 10")
       
   @unittest.expectedFailure
   def test_failFormatMS(self):
       result=formatMS(10000)
       self.assertEqual(result,"not a real result")

   def test_nextTrack(self):
       result=nextTrack()
       self.assertEqual(result,spotifyObject.next_track(deviceID))

   @unittest.expectedFailure
   def test_failNextTrack(self):
       result=nextTrack()
       self.assertEqual(result,"not a real result")
           
   def test_previousTrack(self):
       result=previousTrack()
       self.assertEqual(result,spotifyObject.previous_track(deviceID))

   @unittest.expectedFailure
   def test_failPreviousTrack(self):
       result=previousTrack()
       self.assertEqual(result,"Not a real result")
    
   def test_findActiveGroups(self):
       result=findActiveGroups("Test User")
       self.assertEqual(result,"Test Group\n")

   @unittest.expectedFailure    
   def test_failFindActiveGroups(self):
       result=findActiveGroups("not a real user")
       self.assertEqual(result,"not a real result")

    
   def test_findMyGroups(self):
       result=findMyGroups("Test User")
       self.assertEqual(result,"Test Group\n")


   @unittest.expectedFailure       
   def test_failFindMyGroups(self):
       result=findMyGroups("Not a real user")
       self.assertEqual(result,"not a real result")

    
   def test_checkGroup(self):
       result=checkGroup("Test Group")
       self.assertEqual(result, True)


   @unittest.expectedFailure  
   def test_failCheckGroup(self):
       result=checkGroup("Not a real Group")
       self.assertEqual(result, True)


   def test_checkUser(self):
       result=checkUser("Test User")
       self.assertEqual(result, True)


   @unittest.expectedFailure 
   def test_failCheckUser(self):
       result=checkUser("Not a real User")
       self.assertEqual(result, True)


   def test_checkHost(self):
       result=checkHost("Test Group", "Test User")
       self.assertEqual(result, True)


   @unittest.expectedFailure 
   def test_failCheckHost(self):
       result=checkHost("Fake Group", "Test User")
       self.assertEqual(result, True)       


       
if (__name__=='__main__'):
    unittest.main()
        
        
