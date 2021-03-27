import urllib.request
import re
import requests
import os

from datetime import datetime
now = datetime.now()
dt_string = now.strftime('%d/%m/%Y %H:%M:%S')

cwd = os.getcwd()

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} #You get banned for being a 'bot' so we include user like headers

def downloadImage(url):
    global hdr
    global linkID
    global x
    req = urllib.request.Request(url, headers=hdr)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode('utf-8') #Downloading full website code to regex find the direct image link below
    directLink = re.findall('https:\/\/image\.prntscr\.com\/image\/.{3,22}\.(?:png|jpg|jpeg)', respData) #REFERENCE directLink[0] DUE TO DUPLICATES FORMING AN ARRAY
    if len(directLink) < 1:
        directLink = re.findall('https:\/\/i\.imgur\.com\/.{7}\.(?:png|jpg|jpeg)', respData)
    else:
        pass
    print('Downloaded prnt.sc/'+linkID+x)
   
##    urllib.request.urlretrieve(directLink[0], "Images/"+linkID+".png") #Had to use requests because urlretrieve didn't accept headers which were necessary to prevent bot user blocking

    with open("Images/"+linkID+'/'+linkID+x+".png", "wb+") as currentImg:
        response = requests.get(directLink[0])
        currentImg.write(response.content) #Uses requests module to get the binary data of the online image and overwrite a generated local image with it

logFile = open('Downloaded IDs.txt', 'a')
linkID = input('Enter 5 characters only, the program will iterate through 36 files per run (the missing character): ')
logFile.write(linkID+'[a-z, 0-9]'+" "+dt_string+'\n')
logFile.close()

os.mkdir(cwd+'\\Images\\'+linkID)

for x in chars:
    downloadImage('https://prnt.sc/'+linkID+x)

print('FINISHED SUCCESSFULY')
logFile = open('Downloaded IDs.txt', 'a')
logFile.write('The above ID set ran successfully.'+'\n')
logFile.close()
