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

urle=input("enter ID: ")



scope="user-read-private user-read-playback-state user-modify-playback-state"

try:
    token = util.prompt_for_user_token(urle,scope=scope,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')


except:
    os.remove(f".cache-"+urlID)
    token = util.prompt_for_user_token(urlID,scope=scope,client_id='756f6e8b3ffe477ea87a2a53a56bfb6f',client_secret='37b0f26267004da3bbb636334155aaab',redirect_uri='https://google.com/')


#create spotify object
spotifyObject=spotipy.Spotify(auth=token)

#get current device:
devices=spotifyObject.devices()
print(json.dumps(devices,sort_keys=True,indent=4))
print()
usrID="cabbage777"

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
            print('Attention', "There's no active groups")
        finally:
            print("end")

#Creating a new group. User is automatically the host
def createGroup(groupName):
    global connection
    connect()
    checkUser(usrID)
    #Check to see that there's not already a group with the same name
    if (not checkGroup(groupName)): 
            cursor = connection.cursor()
            cursor.callproc('addGroup',args=(groupName,usrID,1))
            cursor.callproc('addPart',args=(usrID,groupName,1))
            cursor.close()
            connection.commit()
            findMyGroups(usrID,groupName)
    else:
         print("Attention", "GroupName already exist, so group can't be created with this name.")

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
        
#Check if user is already a part of the group:
def checkJoin(groupName):
    print("\n\n\n\n\n\n\n\n\n\nRunning checkJoin() ***********************\n\n\n\n\n\n\n\n\n")
    global connection
    connect()
    if (connection.is_connected()):
        print("\n\n\n\n\n\n\n\n Is Connected\n\n\n\n\n\n\n\n")
        sqlQuery = "select username from isPartOf where group_name='"+groupName+"' and username='"+usrID+"';"
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        if records[0][0] == usrID:
            return True #user is in group
        else:
            return False #user is not in group

#Takes in txt and labels to update labels and text in the Group room.
def joinGroup(groupName):
    global connection
    connect()
    checkUser(usrID)
    #Check to see that there exist a group with with name 'groupName'
    if(checkGroup(groupName)):
        if(not checkJoin(groupName)):
            cursor = connection.cursor()
            cursor.callproc('updateGroupNumber',args=(groupName,))
            cursor.callproc('addIsPartOf',args=(usrID,groupName,0))
            connection.commit()
            cursor.close()
            print('Attention','You have now joined the group '+groupName)
            
        listenToGroup(groupName,usrID)
    else:
         print('Attention',"There's no group named "+groupName)
         return

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

   def test_createGroup(self):
       createGroup("tester12345")
       query = "select group_name from Groups where group_name='tester12345';"
       cursor = connection.cursor()
       cursor.execute(query)
       records = cursor.fetchall()
       result = ""
       try:
           for row in records:
               result = row[0]
       except:
           self.fail()

   def test_joinGroup(self):
       joinGroup("tester12345")

       def test_listenToGroup(self):
            listenToGroup("tester12345", usrID)

       def test_isActive(self):
            connect()
            result = isActive("tester12345")
            self.assertTrue(result)

       def test_checkJoin(self):
            connect()
            result = checkJoin("tester12345")
            self.assertEqual(result, True)      

   def test_database(self):
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


            sqlQuery1 = "select track_uri from GroupPlaying where group_name='Test Group';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery1)
            records = cursor.fetchall()
            for row in records:
                uri=str(row[0])
            sqlQuery2 = "select position from GroupPlaying where group_name='Test Group';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2)
            records = cursor.fetchall()
            for row in records:
                position=row[0]
            trackList=[]
            print(uri)
            trackList.append(uri)
            print(position)
            spotifyObject.start_playback(deviceID,None,trackList)
            spotifyObject.seek_track(int(position), deviceID)
            
           
            
       except Error as e:
              print ("error while connecting to MySQL", e)
       finally:

           def test_URI(self):
               self.assertEqual(uri, "spotify:track:11dFghVXANMlKmJXsNCbNl")

           def test_Position(self):
               self.assertEqual(position, "20")



           if(connection.is_connected()):
               cursor.close()
               connection.close()
               print("MySQL connection is closed")

       
if (__name__=='__main__'):
    unittest.main()


    




