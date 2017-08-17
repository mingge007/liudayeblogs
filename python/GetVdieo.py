#coding=utf-8

import datetime
import re
import urllib2


def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

def getVideoUrl(html,reg):
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

# 格式化数据结构
def formatHtml(atablist,baseurl):
    backStr="";
    hashdict={'a':0}
    j=0
    for atab in atablist:
        p = re.compile(r'[\s]+')
        arr = p.split(atab.strip())
        dict={'url':'','title':'','img':''}
        for i in arr:
            if(i.find('href=')>-1):
                dict['url']=i.replace("href=","").replace("\"","").replace("#vfrm=19-9-0-1","").replace("#vfrm=2-4-0-1","")
            elif  (i.find('title=')>-1):
                dict['title']=i.replace("title=","").replace("\"","")
            elif  (i.find('data-src=')>-1):
                dict['img']=i.replace("data-src=","").replace("\"","")
        if( not hashdict.has_key(dict['title'])):
            backStr += '\t\t\t\t\t\t<a alt="'+dict['title']+'" target="_self" href="'+baseurl+'?src='+dict['url']+'&videoName='+dict['title']+'" >'+dict[
                'title']+'</a>\n'
            hashdict[dict['title']]=1
            if(j==6):
                backStr += '\t\t\t\t\t\t\n<br/>'
                j=1;
            else:
                j=j+1
    return backStr


def getTableHtml(fenxiReg,fenxiName,baseurl):
    backStr="";
    now = datetime.datetime.now()
    nowStr = now.strftime('%Y-%m-%d %H:%M:%S');
    backStr += '\t<table border="0"  cellspacing="0" cellpadding="0">\n'
    ki=0
    for url in fenxiName.keys():
        atablist = getVideoUrl(getHtml(url),fenxiReg[url])
        backStr +='\t\t<tr>\n\t\t\t<td>'
        # print '\t<li>\n<span><p></p>"+fenxiName[url]+"</span>\n<ul>'
        backStr += '\t\t\t\t<div class=up onclick=show("a'+str(ki)+'")>'+fenxiName[url]+' (更新时间：'+nowStr+'）</div><div onmouseover=high() onmouseout=low() id=a'+str(ki)+' ' \
                                                                                                                                                             'style="display:none">\n'
        backStr += formatHtml(atablist,baseurl)
        ki=ki+1
        backStr += "\t\t\t\t\n</div>"
        backStr += "\t\t\t</td>\n\t\t</tr>\n"
    backStr += "</table>\n"
    return backStr

def getVideoJson(fenxiReg,fenxiName):
    for url in fenxiName.keys():
        atablist = getVideoUrl(getHtml(url),fenxiReg[url])
        return atablist