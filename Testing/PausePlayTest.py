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

deviceID=devices['devices'][0]['id']


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

            print("collecting currently playing song")
            sqlQuery1 = "select track_uri from GroupPlaying where group_name='" + group_name + "';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery1)
            records = cursor.fetchall()
            for row in records:
                uri=str(row[0])
            print("URI:", uri)

            print("collecting song position")
            sqlQuery2 = "select position from GroupPlaying where group_name='" + group_name + "';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2)
            records = cursor.fetchall()
            for row in records:
                position=row[0]
            print("Position:", position)

            print("updating song information")
            trackList=[]
            trackList.append(uri)
            spotifyObject.start_playback(deviceID,None,trackList)
            spotifyObject.seek_track(int(position), deviceID)

            paused=spotifyObject.current_user_playing_track()
            print("Is Playing:", paused['is_playing'])

            print("collecting pause value")
            sqlQuery3 = "select isPaused from GroupPlaying where group_name='" + group_name + "';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery3)
            print("fetching results")
            records = cursor.fetchall()
            for row in records:
                isPaused = row[0]
            if isPaused == 1:
                spotifyObject.pause_playback(deviceID)
            paused = spotifyObject.current_user_playing_track()
            print("Is Playing:", paused['is_playing'])
except Error as e:
        print ("error while connecting to MySQL:", e)
finally:

#begin testing suite
    def test_URI(self):
        self.assertEqual(uri, "spotify:track:11dFghVXANMlKmJXsNCbNl")

    def test_Position(self):
        self.assertEqual(position, "20")

    def test_Paused(self):
        if isPaused == 1:
            self.assertEqual(paused['is_playing'], "False")
        elif isPaused == 0:
            self.assertEqual(paused['is_playing'], "True")

    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

if (__name__=='__main__'):
    unittest.main()