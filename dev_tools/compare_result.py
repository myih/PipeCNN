import glob, os, string, array, binascii
import numpy as np
from string import *

data1=[]
data2=[]
i=0
j=0

with open('tvmout.txt', 'r') as file1:
	for line1 in file1:
		for word1 in line1.split():
			data1.append(int(word1))
			#print ("{}".format(data1[i]))
			i=i+1

print ("////////\n\n")


with open('fpgaout.dat', 'r') as file2:
	for line2 in file2:
		for word2 in line2.split():
			data2.append(int(word2))
			#print ("{}".format(data2[j]))
			j=j+1

#np.allclose(data1, data2, 1000)

print ("true") if np.allclose(data1, data2, 0.06) else print("false")