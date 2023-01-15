import json
import socket
import socks
import stem.process
import requests
import time

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

# start TOR


# patch the socket module
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
socket.create_connection = create_connection

print(' \033[35mRooting all your device traffic through TOR Relays\033[0m')

while True:
    tor_process = start_tor('tor')
    print('\033[33mTOR is running\033[0m')
    response = requests.get("http://ipinfo.io/ip")
    url = 'https://ipinfo.io/' + response.text
    response2 = requests.get(url)
    data = response2.json()
    timezone = data.get('timezone')
    print("\033[34mConnected to:\033[0m ", str(response.text) + '     ' + str(timezone))
    time.sleep(300)
    tor_process.kill()
