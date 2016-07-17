import urllib
import xml.etree.ElementTree as ET
import os
import time
import datetime
import json

date = str(datetime.date.today())
path = '/home/zhong/Wallpaper/'+date+'/'

def mkdir(path):
    if not os.path.exists(path):
        print os.path.exists(path)
        os.system('mkdir '+path)

def getJson():
    mkdir(path=path)
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    conn = urllib.urlopen(url)
    f = open(name=path+date+'.json', mode='w')
    f.write(conn.read())
    f.close()

def getImage():
    getJson()
    f = open(name=path+date+'.json',mode='r')
    Json = f.read()
    ImageUrl = json.loads(Json)['images'][0]['url']
    conn = urllib.urlopen(url=ImageUrl)
    Image = open(name=path+date+'.jpg', mode='wb')
    Image.write(conn.read())
    Image.close()
    f.close()


if __name__ == '__main__':
    isNetworkConnected = False
    while not isNetworkConnected:
        res = os.system('ping cn.bing.com -c 1')
        if res:
            time.sleep(60)
        else:
            isNetworkConnected = True
    getImage()
    os.system('gsettings set org.gnome.desktop.background picture-uri "file://'+path+date+'.jpg"')
