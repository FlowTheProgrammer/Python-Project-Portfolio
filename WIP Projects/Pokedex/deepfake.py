from fakeyou import FakeYou
import requests
import os
from pygame import mixer
import pygame
import tempfile

global username
global password

def getLogin():
    global username
    global password
    username = input("Enter Username: ")
    password = input("Enter Password: ")



def getName(name):
    thisClass = FakeYou()
    try:
        thisClass.login(username= username, password = password)
        audio = thisClass.say(text=name, ttsModelToken="TM:f99ax42k43fg")

        this_audio = requests.get(audio.link,stream=True)

        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(this_audio.content)
        temp_file.close()

        mixer.init()
        mixer.music.load(temp_file.name)
        mixer.music.play()

        thisClass.logout()
    except:
        pass




