import PyPDF2
import re
import os
import http.cookiejar
from bs4 import BeautifulSoup
import urllib.request

PAGE = 'http://orangetide.com/graphics_programming_black_book/pdf/'
bookname = 'graphics_programming_black_book.pdf'
cj = http.cookiejar.CookieJar()

proxyhandler = urllib.request.ProxyHandler({'http': '127.0.0.1'})  # Delete this entry if there's not proxy
opener = urllib.request.build_opener(proxyhandler, urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')]

req = opener.open(PAGE)
response = req.read()

soup = BeautifulSoup(response)
pdfs = soup.findAll(name='a', attrs={'href': re.compile('\.pdf')})
merger = PyPDF2.PdfFileMerger()

for pdf in pdfs:
    if 'http://' not in pdf['href']:
        url = PAGE + pdf['href']
    else:
        url = pdf['href']
    try:
        filename = url.split('/')[-1]
        f = opener.open(url)
        data = f.read()
        with open(filename, "wb") as code:
            code.write(data)
    except Exception as e:
        print('cannot obtain url %s' % ( url, ))
        print('from href %s' % ( pdf['href'], ))
        print(e)
    # Merge with pypdf2
    with open(filename, 'rb') as p:
        merger.append(fileobj=p)
merger.write(open(bookname, 'wb'))

# clean downloaded PDF's except for the final one ;)
tempPDFs = [f for f in os.listdir(os.getcwd()) if 'pdf' in f and f != bookname]
for f in tempPDFs:
    os.remove(f)


