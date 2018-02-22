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



imgkit.from_file('/home/pi/hashtagblessed.github.io/index.html', 'blessed.jpg')

from subprocess import Popen
# os.system('convert' '+' '.join(['/home/pi/hashtagblessed.github.io/py/blank.jpg', '/home/pi/hashtagblessed.github.io/py/blessed.jpg'])+' blessed.pdf')
q = Popen(['convert /home/pi/hashtagblessed.github.io/py/blank.jpg /home/pi/hashtagblessed.github.io/py/blessed.jpg blessed.pdf'], shell=True) 
output = q.communicate()[0]


with open("blessed.pdf") as f:
  # call the system's lpr command
  p = Popen(["lpr /home/pi/hashtagblessed.github.io/py/blessed.pdf"], stdin=f, shell=True) 
  output = p.communicate()[0]

time.sleep(45)    

while datetime.datetime.now() > OpenNight:
    schedule.run_pending()
     time.sleep(1)

else:
		p = Popen(['python ./hashpdf.py'], shell=True)  
		output = p.communicate()[0]