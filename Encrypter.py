from time import sleep
from math import *
from decimal import *
import struct

# HELPER functions

def LST_to_STR (lst) :
    str1 = ""
 
    for ele in lst:
        str1 += ele
 
    return str1


def STR_to_LST (str) :
    li = list(str.split(" "))
    return li

# MAIN functions

def encrypt_str (text) :
    to = list(text)

    encrypted_bin_code = []

    for char in to :
        encrypted_bin_code.append(ord(char))

    return encrypted_bin_code

def decrypt_str (bin_value) :
    message = []

    for values in bin_value :
        message.append(chr(values))

    return LST_to_STR(message)

def encrypt_num(num):
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

def decrypt_num(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]
