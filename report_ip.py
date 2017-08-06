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
import smtplib

def Check_NetConnection():
    while True:
        try:
            socket.gethostbyname('www.baidu.com')
        except Exception, e:
            print 'Network connection is not ready'
        else:
            print 'Network connection is ready'
            break
        time.sleep(1)

def Get_LocalIpAddress():
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    skt.connect(('8.8.8.8', 80))
    socketIpPort = skt.getsockname()
    ip = socketIpPort[0]
    skt.close()

    return ip

def Send_IpAddressEmail(ip):
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com", "25")
    smtp.login('wangge1989@126.com', '')
    smtp.sendmail('wangge1989@126.com', \
                  'wangge1989@126.com', \
                  'From: wangge1989@126.com\r\n' +\
                  'To: wangge1989@126.com\r\n' +\
                  'Subject: Raspberry IP Address: ' +\
                  ip +\
                  '\r\n\r\nAs subject.')
    print 'IP Address report Email is sent to wangge1989@126.com'
    smtp.quit()

def main():
    Check_NetConnection()
    Send_IpAddressEmail(Get_LocalIpAddress())

if __name__ == "__main__":
    main()
