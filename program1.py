import urllib2
import re
from BeautifulSoup import BeautifulSoup
import sys

def prepareSource(urlAddr):
    if(not urlAddr.startswith("http://")):
        urlAddr = "http://"+urlAddr
    response = urllib2.urlopen(urlAddr)

    f = open('source.html','w')
    ftxt = open('source.txt','w')

    html = response.read()
    f.write(html)
    response.close()
    f.close()

    html = re.sub("<!.*>","",html)
    soup = BeautifulSoup(html)

    for script in soup(["script", "style"]):
        script.extract()    


    text = ''.join(soup.findAll(text=True)).encode('utf-8').strip()

    #manual tag removal
    tags = ["<div.*?>","</div>","<p>","</p>","<br />","<a.*\">","<a>","</a>"]
    for tag in tags:
        text = re.sub(tag, "",text)

    lines =(line.strip() for line in text.splitlines())
    chunks =(phrase.strip() for line in lines for phrase in line.split(" "))
    all_text = ' '.join(chunk for chunk in chunks if chunk)

    #remove punctuation marks
    chars =['.','-',',',';','?',':','!','...',"(",")",'"']
    for char in chars:
        all_text = all_text.replace(char, "")

    ftxt.write(all_text)
    ftxt.close()

def start():
    url = raw_input("--Enter url: ")

    prepareSource(url)
    print 'Done'
    

if __name__ == "__main__":
    start()
