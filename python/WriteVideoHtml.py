#coding=utf-8
import  GetVdieo

# retStr = GetVdieo.getVideoJson(fenxiReg, fenxiName, baseurl)

def do(fenxiReg,fenxiName,baseurl,fileName):
    retStr = GetVdieo.getTableHtml(fenxiReg, fenxiName, baseurl)

    fileHandle = open (fileName, 'w')
    fileHandle.write (retStr)

