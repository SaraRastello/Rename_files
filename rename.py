from __future__ import division  
import fileinput
import matplotlib.pyplot as plt
import plotly.plotly as py
import glob
from natsort import realsorted, ns
import os


files=realsorted(glob.glob('cia*.txt'))
N=len(files)
print files
#for fname in filenames:
for j in range(N):
	os.rename('cia*.txt', 'sara*.txt')
	

print 'ok' 