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
import pyttsx

def Check_NetConnection():
    engine = pyttsx.init()
    engine.setProperty('rate', 110)
    while True:
        try:
            socket.gethostbyname('www.baidu.com')
        except Exception, e:
            engine.say('Network connection is not ready yet')
            engine.runAndWait()
        else:
            engine.say('Network connection is ready')
            engine.runAndWait()
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
    engine = pyttsx.init()
    engine.setProperty('rate', 110)
    engine.say('You IP Address is')
    engine.runAndWait()
    time.sleep(0.5)

    for i in range(4):
        engine.say(ip.split('.')[i])
        if (3 != i):
            engine.say('dot')
        engine.runAndWait()
        time.sleep(0.5)

def main():
    Check_NetConnection()

    for i in range(10):
        Speak_IpAddress(Get_LocalIpAddress())
        time.sleep(5)

if __name__ == "__main__":
    main()
