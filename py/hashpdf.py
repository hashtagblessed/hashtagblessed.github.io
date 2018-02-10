import pdfkit



options = {
    'page-size': 'Letter',
    'encoding': "UTF-8",
    'javascript-delay': 1000,
  


}


pdfkit.from_file('/Users/chrisgivens/hashtagblessed.github.io/index.html', 'out.pdf', options=options)

#pdfkit.from_url('https://hashtagblessed.github.io/', 'out.pdf', options=options)