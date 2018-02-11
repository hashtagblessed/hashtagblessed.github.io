import pdfkit
import os


options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    #'javascript-delay': 100,
  	'encoding': 'UTF-8',

}


pdfkit.from_file('/Users/chrisgivens/hashtagblessed.github.io/index.html', 'out.pdf', options=options)

os.startfile("YourDocument", "print")

#pdfkit.from_url('https://hashtagblessed.github.io/', 'out.pdf', options=options)