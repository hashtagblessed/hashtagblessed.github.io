#!/usr/bin/env python
import os
import pdfkit
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

options = {
    'page-size': 'Letter',
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in',
  	'encoding': 'UTF-8',
  	'zoom': 1.246,

}


pdfkit.from_file('/Users/chrisgivens/hashtagblessed.github.io/index.html', 'blessed.pdf', options=options)

time.sleep(0.2)

from subprocess import Popen
with open("blessed.pdf") as f:
  # call the system's lpr command
  p = Popen(["lpr"], stdin=f, shell=True) 
  output = p.communicate()[0]

time.sleep(45)    

while datetime.datetime.now() > OpenNight:
    schedule.run_pending()
     time.sleep(1)

else:
		p = Popen(['python ./hashpdf.py'], shell=True)  
		output = p.communicate()[0]