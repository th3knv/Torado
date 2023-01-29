#!/usr/bin/env python3

import subprocess
import socket
import socks
import stem.process
import time
import requests

print('''\033[0;33m
Check for TOR if it's running (Cause it may prints error)
$ sudo lsof -i :9050
----------------------------------------------------------
Kill TOR service
$ sudo kill -9 <PID>
----------------------------------------------------------
Disable gsettings proxy in case of error (You won't be able to access a webiste)
$ gsettings set org.gnome.system.proxy mode none
--------------------------------------------------------------------------------- 
\033[0;33m''')
print('\033[0;34mFor any kind of error please, open a pull request. I will be always active\033[0;32m')
print('')
print("""\033[0;32mSometimes you need to wait if program prints 'Expecting value' and 'HTTPConnectionPool error'
For any kind of error please, open a pull request. I will be always active\033[0;32m""")


def start_tor(tor_path='tor'):
  tor_process = stem.process.launch_tor_with_config(
    tor_cmd=tor_path,
    config = {
      'SocksPort': str(9050)
    },
  )
  return tor_process

def create_connection(address, timeout=None, source_address=None):
  sock = socks.socksocket()
  sock.connect(address)
  return sock

#Set browser config

subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "mode", "'manual'"])
subprocess.run(["gsettings", "set", "org.gnome.system.proxy.socks", "host", "'127.0.0.1'"])
subprocess.run(["gsettings", "set", "org.gnome.system.proxy.socks", "port", "9050"])

# start TOR
tor_process = start_tor('tor')

# patch the socket module
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
socket.create_connection = create_connection
print('')
print('')
print('\033[35mRouting all your device traffic through TOR Network\033[0m')

while True:
    print('\033[33mTOR is running\033[0m')
    try:
        response = requests.get("http://ipinfo.io/json")
        data = response.json()
        ip = data['ip']
        timezone = data['timezone']
        print("\033[34mConnected to:\033[0m ", ip + '     ' + timezone)
        time.sleep(100)
    except requests.exceptions.RequestException as e:
        subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "mode", "'none'"])
        print("\033[31mError occured:", e,"\033[0m")
    except KeyboardInterrupt:
        tor_process.kill()
        subprocess.run(["gsettings", "set", "org.gnome.system.proxy", "mode", "'none'"])
        print("\033[35mTOR process stopped\033[0m")
        break
