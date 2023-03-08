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


class Conversions:
    def Decimal_To_Binary(decimal: int=0):
        return bin(decimal).replace("0b", "")
    def Binary_To_Decimal(binary):
        return int(binary, 2)