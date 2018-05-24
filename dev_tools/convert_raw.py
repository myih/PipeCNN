
import glob, os, string, array, binascii
from string import *


rawFile = open('rawimage.dat',"wb")
File = open('inputs.txt',"rb")
for line in File:
    for word in line.split():
        bytestring=int(float(word)*127).to_bytes(1, 'big')
        print ("{}".format(bytestring))
        rawFile.write(bytestring)
rawFile = open('rawweight.dat',"wb")
File = open('weights.txt',"rb")
for line in File:
    for word in line.split():
        bytestring=int(float(word)*127).to_bytes(1, 'big')
        print ("{}".format(bytestring))
        rawFile.write(bytestring)
rawFile = open('tvmout.txt',"w")
File = open('output.txt',"rb")
for line in File:
    for word in line.split():
        #bytestring=int(word*127).to_bytes(1, 'big')
        #print ("{}".format(float(word)*127))
        rawFile.write(str(int(float(word)*127*127)))
        rawFile.write(" ")
    rawFile.write("\n")
