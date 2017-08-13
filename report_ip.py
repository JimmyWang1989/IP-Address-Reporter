#!/usr/bin/python
#-*-coding:utf-8-*-
#
# Copyright (C) 2017 Wang Ge
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, in version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import socket
import time
import pygame
import os
from aip import AipSpeech

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

def Check_NetConnection():
    pygame.mixer.init(frequency = 16000)
    track = pygame.mixer.music.load("voice/connect.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    print 'Connecting...'

    while True:

        try:
            socket.gethostbyname('www.baidu.com')
        except Exception, e:
            print 'Network connection is not ready yet'
        else:
            print 'Network connection is ready'
            track = pygame.mixer.music.load("voice/connected.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            break
        time.sleep(5)

def Get_LocalIpAddress():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    skt.connect(('www.baidu.com', 80))
    socketIpPort = skt.getsockname()
    ip = socketIpPort[0]
    skt.close()

    return ip

def Speak_IpAddress(ip):
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result  = aipSpeech.synthesis('你的IP地址是' + ip, 'zh', 1, {
        'vol': 5,
    })

    if not isinstance(result, dict):
        with open('voice/ip.mp3', 'wb') as f:
            f.write(result)

    print 'Your IP Address is ' + ip
    pygame.mixer.init(frequency = 16000)
    track = pygame.mixer.music.load("voice/ip.mp3")
    pygame.mixer.music.play()

    # pygame.mixer.music.play()
    for i in range(6):
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        time.sleep(10)

def main():
    if os.path.isfile('voice/ip.mp3'):
        os.remove('voice/ip.mp3')
    Check_NetConnection()
    Speak_IpAddress(Get_LocalIpAddress())

if __name__ == "__main__":
    main()
