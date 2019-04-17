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
            print ("you're connected to - ", record)


            sqlQuery1 = "select track_uri from GroupPlaying where group_name='byteme';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery1)
            records = cursor.fetchall()
            for row in records:
                uri=str(row[0])
            sqlQuery2 = "select position from GroupPlaying where group_name='byteme';"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2)
            records = cursor.fetchall()
            for row in records:
                position=row[0]
            trackList=[]
            print(uri)
            trackList.append(uri)
            positionList=[]
            positionList.append(int(position))
            print(position)
            spotifyObject.start_playback(deviceID,None,trackList)
            spotifyObject.seek_track(int(position), deviceID)
            
           
            
except Error as e:
        print ("error while connecting to MySQL", e)
finally:

    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")




