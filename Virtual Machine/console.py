import tkinter.messagebox
import asyncio
import csv
import getpass
import json
import os
import random
import select
import selectors
import socket
import string
import sys
import time
import base64
import tkinter
import contextlib
import warnings
import errno
import encodings
import struct
import binascii
import collections
import collections.abc
import contextlib
import functools
import operator
import re
import types
import platform
import pickle
from abc import abstractmethod, ABCMeta
from distutils.core import setup


with open("userdata.enz", "r") as file:
    userdata = file.read().split("\n")

with open("directories.enz", "r") as file:
    directories = file.read().split("\n")

userdata.remove("")
directories.remove("")
path: str = "~/Desktop"  # This is the default path for whenever you turn on the machine
end: str = ">"  # The end point that shows up at the end
Running: bool = True  # Tells the program wether or not its still running
username: str = userdata[0]  # Username that is saved
password: str = userdata[1]  # Password that is saved
IsRequiredOnStartUp: str = userdata[2]
AdminPassword: str = userdata[3]
IsAdmin: bool = False


def InstallPackage(pn):
    try:
        source_url = "https://raw.githubusercontent.com/RavinClaw/Virtual-Machine-Packages/main/"
        print("Installing from: " + source_url + pn + "/" + pn + ".py")
        os.system("curl " + source_url + pn + "/" + pn +
                  ".py --output packages/" + pn + ".py")
        return "Package " + pn + " Installed Successfully"
    except:
        print("Unable to complete download...")
        return "E:\\ This package does not exist"


print("\t\t\t\t\t\t\t\t\tNecronOS Base Console\n\n")
while Running == True:
    zeno = input(path + end)
    if zeno[0:3] == "cd ":
        selectpath = zeno[3:]
        for dir in directories:
            if selectpath == dir:
                path = selectpath
            else:
                continue

    elif zeno[0:4] == "sudo":
        if zeno[5:12] == "install" and IsAdmin:
            package_name = zeno[14:]
            response = ""
            response = InstallPackage(pn=package_name)
            print(response)

        elif zeno[5:12] == "install" and not IsAdmin:
            attempts = 3
            cpassword = getpass.getpass("Sudo Password: ")
            while not cpassword == AdminPassword and attempts >= 1:
                attempts -= 1
                print("Sudo Password Incorrect: ", attempts, "attempts left")
                cpassword = getpass.getpass("Sudo Password: ")
            if not attempts >= 1:
                print("Sudo Login Canceled due to running out of attempts")
            else:
                print("Login Successful")
                IsAdmin = True

        elif zeno[5:10] == "login" and not IsAdmin:
            attempts = 3
            cpassword = getpass.getpass("Sudo Password: ")
            while not cpassword == AdminPassword and attempts >= 1:
                attempts -= 1
                print("Sudo Password Incorrect: ", attempts, "attempts left")
                cpassword = getpass.getpass("Sudo Password: ")
            if not attempts >= 1:
                print("Sudo Login Canceled due to running out of attempts")
            else:
                print("Login Successful")
                IsAdmin = True

        elif zeno[5:10] == "login" and IsAdmin:
            print(username, "is already authorized")

    elif zeno[0:5] == "clear":
        if os.name == "nt":
            cls = "cls"
        else:
            cls = "clear"
        os.system(cls)

    elif zeno[0:6] == "system":
        if zeno[7:16] == "-shutdown":
            print("System is shutting down...")
            Running = False

    elif zeno[0:5] == "mkdir":
        if zeno[6:8] == "./":
            newpath = zeno[8:]
            createpath = path + "/" + newpath
            directories.append(createpath)
        else:
            createpath = zeno[6:]
            directories.append(createpath)

    elif zeno[0:2] == "ls":
        currentpathextension = path + "/"
        for dir in directories:
            if not currentpathextension == dir[0:len(currentpathextension)]:
                continue
            else:
                print(dir)

    elif zeno[0:7] == "python3":
        python = zeno[8:]
        if len(python) > 0:
            command = "python " + str(python)
            os.system(command)
        else:
            print("Cannot Use Python3 without commands as it crashes the machine")

sys.exit()
