from BeautifulSoup import BeautifulSoup
from zad1 import prepareSource
import re
import socket
import subprocess
import urlparse

internal = [] #url internal
external = [] #url external

url = raw_input("...Enter url: ")
base_ip = socket.gethostbyname(url) #ip 
internal.append(url)
level = 0 #deep (0 - root)
index = 0 #index of last element in list for particular level

localSources = open("localSources.txt","w")
externalSources = open("ExternalSources.txt","w")

def extractUrls():
    print " ==== Poziom: "+ str(level) + " ===="
    for address in internal[index-1:]:
        internalCounter = 0
        print "przetwarzam adres "+address
        print "LEN: "+str(len(internal))
        prepareSource(address)
        path = 'source.html'
        htmlFile = open(path,'r')
        soup = BeautifulSoup(htmlFile)
        for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
            href= link.get('href').replace('http://','')
            href = urlparse.urlparse(href)
            href = re.sub('/.*','',href.path).replace(" ",'')
            
            try:
                IPaddr = socket.gethostbyname(href)
            except socket.gaierror as ex:
                print "Not found"
                
            if(IPaddr == base_ip):
                if href not in internal: 
                    internal.append(href)
                    print "local: "+href
                    internalCounter += 1
            else:
                if href not in external:
                    external.append(href)
                    print "external: " + href
                    
            for i in internal:
                localSources.write(i+'\n')
            for i in external:
                externalSources.write(i+'\n')
        htmlFile.close()
        print "Na poziomie "+str(level)+" znaleziono "+str(internalCounter)+" wewn. linkow"
                
while level < 3:
    extractUrls()
    index = len(internal)
    level += 1
    
localSources.close()
externalSources.close()
