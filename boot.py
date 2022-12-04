import os
import socket
import string
import random
import subprocess
import sys
import time

def Checking_System():
  continuation = False
  print("Checking the system")
  host = socket.gethostname()
  ip = socket.gethostbyname(host)
  if os.path.exists("unix.py"):
    print("Unix VM System has been found")
    continuation = True
  else:
    print("Unix VM System could not be found")
    continuation = False
  return continuation, host, ip


def Initiate():
  cont = False
  host = ""
  ip = ""
  print("Starting Process")
  if not __name__ == "__main__":
    cont, host, ip = Checking_System()
  print(f"Host: {host}\tIP: {ip}\tContinue?: {cont}")
  

Initiate()
