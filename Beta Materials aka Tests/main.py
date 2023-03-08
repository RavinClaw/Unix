import os
import sys
from binary import Conversions
import msvcrt

while True:
    character = msvcrt.getwch()
    luck = Conversions.Decimal_To_Binary(ord(character))
    if not luck == "1000":
        print(luck)
    else:
        sys.exit()