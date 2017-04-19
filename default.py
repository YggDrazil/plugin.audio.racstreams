#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,sys,xbmcaddon,base64

pluginhandle = int(sys.argv[1])
settings = xbmcaddon.Addon(id='plugin.audio.radioteddy_de')

forceViewMode=settings.getSetting("forceViewMode")
if forceViewMode=="true":
  forceViewMode=True
else:
  forceViewMode=False
viewMode=str(settings.getSetting("viewMode"))

def index():
        addLink("Division Germania - Manifest","https://archive.org/download/DivisionGermaniaManifest/tmp_2516-Division%20Germania%20-%20Manifest-865126730.mp3",'playAudio',"https://img.discogs.com/VpnWBdTRWOf-aHYvxvxHP4zqj6o=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-3490208-1350501736-8167.jpeg.jpg")
        addLink("Blutlinie - Tag der Abrechnung ","https://archive.org/download/TagDerAbrechnung/Blutlinie%20Full%20Album%202016.mp3",'playAudio',"http://opos-records.com/images/product_images/popup_images/3330_0.jpg")
        addLink("Kinder Disco","http://streams.ir-media-tec.com/radioteddy-ch02.mp3",'playAudio',"http://webplayer.radioteddy.de/img/_channels/_header/ch02.png")
        addLink("Soft Mix","http://streams.ir-media-tec.com/radioteddy-ch06.mp3",'playAudio',"http://webplayer.radioteddy.de/img/_channels/_header/ch06.png")
        addLink("Gute Nacht Musik","http://streams.ir-media-tec.com/radioteddy-ch03.mp3",'playAudio',"http://webplayer.radioteddy.de/img/_channels/_header/ch03.png")
        addLink("Weihnachtslieder","http://streams.ir-media-tec.com/radioteddy-ch07.mp3",'playAudio',"http://webplayer.radioteddy.de/img/_channels/_header/ch07.png")
        addLink("Kinderlieder","http://streams.ir-media-tec.com/radioteddy-ch04.mp3",'playAudio',"http://webplayer.radioteddy.de/img/_channels/_header/ch04.png")
        addLink("TEDDY Cool","http://streams.ir-media-tec.com/radioteddy-ch01.mp3",'playAudio',"http://webplayer.radioteddy.de/img/_channels/_header/ch01.png")
        xbmcplugin.endOfDirectory(pluginhandle)
        if forceViewMode==True:
          xbmc.executebuiltin('Container.SetViewMode('+viewMode+')')

def playAudio(url):
        if url.find(".m3u")>=0:
          url=getUrl(url)
        listitem = xbmcgui.ListItem(path=url)
        return xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)

def cleanTitle(title):
        title=title.replace("&lt;","<").replace("&gt;",">").replace("&amp;","&").replace("&#039;","\\").replace("&quot;","\"").replace("&szlig;","ß").replace("&ndash;","-")
        title=title.replace("&Auml;","Ä").replace("&Uuml;","Ü").replace("&Ouml;","Ö").replace("&auml;","ä").replace("&uuml;","ü").replace("&ouml;","ö")
        title=title.strip()
        return title

def getUrl(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0')
        response = urllib2.urlopen(req,timeout=60)
        link=response.read()
        response.close()
        return link

def parameters_string_to_dict(parameters):
        ''' Convert parameters encoded in a URL to a dict. '''
        paramDict = {}
        if parameters:
            paramPairs = parameters[1:].split("&")
            for paramsPair in paramPairs:
                paramSplits = paramsPair.split('=')
                if (len(paramSplits)) == 2:
                    paramDict[paramSplits[0]] = paramSplits[1]
        return paramDict

def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
         
params=parameters_string_to_dict(sys.argv[2])
mode=params.get('mode')
url=params.get('url')
if type(url)==type(str()):
  url=urllib.unquote_plus(url)

if mode == 'playAudio':
    playAudio(url)
else:
    index()
