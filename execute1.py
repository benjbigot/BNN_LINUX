import os,sys,time,re
from subprocess import Popen, list2cmdline
import subprocess
import multiprocessing as mp
from duplicate import *
from glob import glob
from os import rename
def execution(a,b):
		#path='C://xampp/htdocs/bnn/'
		#path=os.getcwd()
		path='/opt/lampp/htdocs/bnn/'
		os.chdir(path)
		#subprocess.call("youtube-dl.exe -o "+b+".mp4 "+a,shell=True)
		print subprocess.call("/usr/bin/youtube-dl -o "+path+a+".mp4 "+b,shell=True)
if __name__ == "__main__":
    if len(sys.argv) != 3 or "--help" in sys.argv:
        print "not available"
        sys.exit(-1)
    else:
        execution(sys.argv[1],sys.argv[2])


