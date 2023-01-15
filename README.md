# Torado
A script that roots all your machine traffic through TOR Network

## Note that you may need to run scrip with admin privilages

# Downloading Tor

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
## For Windows
```
C:\> netstat -ano | findstr :9050
```
**Find the PID number and KILL the task**
```
C:\> taskkill /PID (PID number)          without these ()
```
## For Linux
```
❯ sudo lsof -i :9050
```
**Find the PID number and KILL the task**
```
❯ sudo kill -9 (PID number)              without these ()


