#!/usr/bin/env python
import os
import pdfkit
import time
import subprocess



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

try:
	while True:
		p = Popen(['python ./hashpdf.py'], shell=True)  
		output = p.communicate()[0]
except KeyboardInterrupt:
  exit
