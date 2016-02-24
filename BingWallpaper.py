import urllib
import xml.etree.ElementTree as ET
import os
import time
import datetime

date = str(datetime.date.today())
path = '/home/zhong/Wallpaper/'+date+'/'

def mkdir(path):
    if not os.path.exists(path):
        print os.path.exists(path)
        os.system('mkdir '+path)

def getXML():
    mkdir(path=path)
    xmlurl = 'http://az517271.vo.msecnd.net/TodayImageService.svc/HPImageArchive?mkt=zh-cn&idx=0'
    conn = urllib.urlopen(xmlurl)
    f = open(name=path+date+'.xml', mode='w')
    f.write(conn.read())
    # XML = conn.read()
    f.close()

def getImage():
    getXML()
    f = open(name=path+date+'.xml',mode='r')
    tree = ET.ElementTree(file=f)
    root = tree.getroot()
    fullImageUrl = root[6].text
    Image = open(name=path+date+'.jpg', mode='wb')
    conn = urllib.urlopen(url=fullImageUrl)
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
