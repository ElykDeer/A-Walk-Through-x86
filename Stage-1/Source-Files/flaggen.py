#!/usr/bin/env python2

import sys

xor_key = (ord('E') | ord('l')) & (ord('y') | ord('k'))

if len(sys.argv) != 2:
    print("Usage: ./flaggen.py 'flag'")
    exit(1)

flag = sys.argv[1]

encrypted = ""
for c in flag:
    encrypted += chr((ord(c) << 1) ^ xor_key)
# print(repr(encrypted))  # Proof it works

decrypted = ""
for c in encrypted:
    decrypted += chr((ord(c) ^ xor_key) >> 1)
# print(decrypted)  # Proof it works

nasmString = ''
for c in encrypted:
    nasmString += hex(ord(c)) + ', 0x1f, '

nasmString = nasmString[:-2]

with open("flag.txt", 'w') as f:
    f.write("db " + nasmString + "\n")