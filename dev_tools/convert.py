
import glob, os, string, array, binascii
from string import *


rawFile = open('rawweight.dat',"wb")
File = open('weight.dat',"rb")
for line in File:
    for word in line.split():
        bytestring=int(word).to_bytes(1, 'big')
        print ("{}".format(bytestring))
        rawFile.write(bytestring)
rawFile = open('rawimage.dat',"wb")
File = open('image.dat',"rb")
for line in File:
    for word in line.split():
        bytestring=int(word).to_bytes(1, 'big')
        print ("{}".format(bytestring))
        rawFile.write(bytestring)

