#!/usr/bin/env python
import os
import imgkit
import threading
import time
import datetime
import schedule
import subprocess

OpenNight = datetime.datetime(2018, 02, 23, 23, 15, 0)

def typeforce():
     p = Popen(['for run in {1..5}; do python ./hashpdf.py; done'], shell=True)  
     output = p.communicate()[0]

schedule.every().day.at("15:00").do(typeforce) 



imgkit.from_file('/Users/jormarti2/hashtagblessed.github.io/index.html', 'output.jpg')


time.sleep(0.2)
 
from subprocess import Popen
with open("blessed.pdf") as f:
  # call the system's lpr command
  p = Popen(["lpr output.jpg blank.jpg"], stdin=f, shell=True) 
  output = p.communicate()[0]

time.sleep(45)    

while datetime.datetime.now() > OpenNight:
    schedule.run_pending()
     time.sleep(1)

else:
		p = Popen(['python ./hashpdf.py'], shell=True)  
		output = p.communicate()[0]