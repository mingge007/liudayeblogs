#coding=utf-8

import WriteVideoHtml

# 网址解析正则
fenxiReg={
    "http://www.iqiyi.com/dianying/":r'<a class="site-piclist_pic_link"([\d\D]+?)>',
    "http://www.iqiyi.com/zongyi/":r'(href="http://www.iqiyi.com/v[\d\D]+?title=[\d\D]+?)>',
    "http://www.iqiyi.com/dongman/":r'(href="http://www.iqiyi.com/v[\d\D]+?title=[\d\D]+?)>',
    "http://list.iqiyi.com/www/1/----------2---11-1-1-iqiyi--.html":r'(href="http://www.iqiyi.com/v[\d\D]+?title=[\d\D]+?)>'
    # ,"http://list.iqiyi.com/www/2/----------2---11-1-1-iqiyi--.html":r'(href="http://www.iqiyi.com/a[\d\D]+?title=[\d\D]+?)>'
}
fenxiName={
    "http://www.iqiyi.com/dianying/":"爱奇艺-电影",
    "http://www.iqiyi.com/zongyi/":"爱奇艺-综艺",
    "http://www.iqiyi.com/dongman/":"爱奇艺-动漫",
    "http://list.iqiyi.com/www/1/----------2---11-1-1-iqiyi--.html":"爱奇艺-vip电影"
    # ,"http://list.iqiyi.com/www/2/----------2---11-1-1-iqiyi--.html":"爱奇艺-电视剧"
}

#程序开始
#分析主站
#baseurl1='http://localhost:63342/lsof_java1/vip/videoT.html'
#fileName1 = "/home/lhm/gtest/liudayeblogs/vip/table.html"


#fileName2 = "E:/ideaWorkspace/gitws/lsof_java1/vip/table.html"

fileName = "/home/lhm/gtest/liudayeblogs/source/vip/table.html"
baseurl='http://www.liudaye.com/vip/video.html'

WriteVideoHtml.do(fenxiReg, fenxiName, baseurl, fileName)
# WriteVideoHtml.do(fenxiReg, fenxiName, baseurl1, fileName1)
