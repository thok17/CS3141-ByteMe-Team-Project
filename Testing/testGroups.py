from tkinter import*
import unittest
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

urle=input("enter ID: ")
syncGroup = ""



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

deviceID=devices['devices'][0]['id']
#Getting user id
user=spotifyObject.current_user()
usrID=user['id']

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

#Check if user is in User table, if not it adds the user to User table
def checkUser(usrID):
    global connection
    if (connection.is_connected()):
        sqlQuery = "select username from User where username="+"'"+usrID+"'";
        cursor = connection.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()
        try:
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
        print(records[0][0])
        if records[0][0] == usrID:
            return True #user is in group
        else:
            return False #user is not in group

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
        print("Attention","error while connecting to MySQL")

#Check if group is avtive, then listens to the group       
def listenToGroup(groupName,usrID):
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
        print('Attention',"You you just left group "+syncGroup)
        
    
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
                connection.close()
                findActiveGroups(usrID)
            except Error as e:
                    print('attention',"error while connecting to MySQL")
        syncToGroup() ##This function needs to check the isHost variable and push/pull accordingly
    else:
        print('Attention',"You can't listen to the group "+groupName+",because it's inactive")

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
    except Error as e:
        print("her er feilen")
        print('attention',"error while connecting to MySQL")

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
                print('attention',"Can't listen to this group anymore, because host has left!")
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
        print('Attention',"error while connecting to MySQL")

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
                print(row)
                
        except:
            print("No active groups")

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

def disconnect():
    global connection
    if(connection.is_connected()):
        connection.close()

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
            print ("you're connected to -", record)

            group_name = input("Enter the group name: ")

            #create spotify object
            spotifyObject=spotipy.Spotify(auth=token)

            #get current device:
            devices=spotifyObject.devices()
            print(json.dumps(devices,sort_keys=True,indent=4))
            print()
            deviceID=devices['devices'][0]['id']
            
except Error as e:
        print ("error while connecting to MySQL:", e)
finally:

    #begin testing suite
    class TestCode(unittest.TestCase):
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

        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if (__name__=='__main__'):
    unittest.main()