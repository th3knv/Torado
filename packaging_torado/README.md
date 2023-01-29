# Torado
A script that routes all your machine traffic through TOR Network. It changes IP every 5 minutes (change it in your needs)

## There are 2 versions. 'Torado.py' is for everything. You just have to setup proxy. The 2nd version 'torado_browseronly.py'is only for browsers without setting up something. Ofcourse you can set also the 2nd version to work for everything too

#### Now either you setup your machine with SOCK5 proxy 127.0.0.1:9050 or you setup proxy in a software (from settigns as usually)
#### Note that you may need to run scrip with admin privilages

## Downloading Tor

## Firstly you need to install requirements.txt file. Open the text and install the pips 

## For Windows

**1)** Download TOR Windows version from [here](https://www.torproject.org/download/)

**2)** Configure TOR and make sure it is running correctly

**3)** Locate **tor.exe** (Not the browser) It's an cmd program

**4)** Copy path and paste it in **Torad.py**   / line: 8 /  ***def start_tor(tor_path='PATH\TO\tor.exe')***

**5)** Do the same in line: 33 ***tor_process = start_tor('PATH\TO\tor.exe')***

## For Linux 

**1)** Download TOR with the following commands
### For Debian
```
sudo apt-get install tor
```
### For Arch Linux
```
sudo pacman -S tor
```
## TO RUN TOR
```
sudo systemctl start tor
```
**Check if it's running**
```
sudo systemctl status tor
```
**You're All set**

# If this error occures in every OS
```   raise OSError('Process terminated: %s' % last_problem)
OSError: Process terminated: Failed to bind one of the listener ports.
```
## Check for bind ports
## For Windows open CMD and run it as Administrator
```
netstat -ano | findstr :9050
```
**Find the PID number and KILL the task**
```
taskkill /PID (PID number)          without these ()
```
## For Linux
```
sudo lsof -i :9050
```
**Find the PID number and KILL the task**
```
sudo kill -9 (PID number)              without these ()
```
## IF errors still pops up TOR Service is running. Stop the TASK
```
sudo systemctl stop tor
```


