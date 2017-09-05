---
title: Selenium学习
date: 2017-07-17 16:42:02
tags:
- 学习笔记
- python
- 测试
categories: 学习
#评论
comments: ture
#打赏
reward: true
toc: true
---
# 介绍Selenium
Selenium 是什么？一句话，自动化测试工具。它支持各种浏览器，包括 Chrome，Safari，Firefox 等主流界面式浏览器，如果你在这些浏览器里面安装一个 Selenium 的插件，那么便可以方便地实现Web界面的测试。换句话说叫 Selenium 支持这些浏览器驱动。Selenium支持多种语言开发，比如 Java，C，Ruby等等，而对于python，当然也是支持的！
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=450 src="//music.163.com/outchain/player?type=0&id=575073602&auto=0&height=430"></iframe>
# 安装python
https://www.python.org/downloads/ 下载python3不要在首页直接点下载，要根据电脑选择适合的安装包
https://www.python.org/downloads/release/python-362/ 选【Windows x86-64 executable installer】版本
<!-- more -->
安装时选择自定义目录，添加path，和下载基本库，debug等等选项。

组合按键：win+r，输入：sysdm.cpl，选择高级，查看环境变量是否都配置完整
例如
主目录：D:\Python36\
脚本目:录D:\Python36\Scripts\
组合按键：win+r，输入cmd,打开命令行界面，输入python  \pip3 -V 分别检测安装情况

```shell
C:\Users\liudaye>python
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()			//输入quit退出

C:\Users\liudaye>pip3 -V
pip 9.0.1 from d:\python36\lib\site-packages (python 3.6)

```
# 安装selenium
pip3 install
```shell
C:\Users\liudaye>pip3 install selenium
Collecting selenium
  Downloading selenium-3.5.0-py2.py3-none-any.whl (921kB)
    100% |████████████████████████████████| 921kB 1.0MB/s
Installing collected packages: selenium
Successfully installed selenium-3.5.0

```

# 安装驱动
下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads
选择最新版本，下载后配置环境变量path 增加D:\chromedriver_win32
# 测试自动化
```shell
C:\Users\liudaye>python
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> browser = webdriver.Chrome()
>>> browser.get('http://www.baidu.com/')
>>>
```
运行这段代码，会自动打开浏览器，然后访问百度。
[![http://omucyxh0n.bkt.clouddn.com/20170516200431976.png?imageView2/0/q/75|watermark/2/text/5YiY5aSn54i3/font/5a6L5L2T/fontsize/480/fill/IzAwMDAwMA==/dissolve/100/gravity/SouthEast/dx/10/dy/10|imageslim "自动效果")](http://omucyxh0n.bkt.clouddn.com/20170516200431976.png?imageView2/0/q/75|watermark/2/text/5YiY5aSn54i3/font/5a6L5L2T/fontsize/480/fill/IzAwMDAwMA==/dissolve/100/gravity/SouthEast/dx/10/dy/10|imageslim "自动效果")


 Linux的环境变量也好设置，在~/.bashrc文件中export即可，记得source ~/.bashrc。

    当然，你不设置环境变量也是可以的，程序可以这样写：
```shell
C:\Users\liudaye>python
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>from selenium import webdriver
>>>browser = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
>>>browser.get('http://www.baidu.com/')
>>>
```
# 模拟提交
运行一下python代码
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source)
```
[![自动效果](http://omucyxh0n.bkt.clouddn.com/20170516200636651.gif?imageView2/0/q/75|watermark/2/text/5YiY5aSn54i3/font/5a6L5L2T/fontsize/480/fill/IzAwMDAwMA==/dissolve/100/gravity/SouthEast/dx/10/dy/10|imageslim "自动效果")](http://omucyxh0n.bkt.clouddn.com/20170516200636651.gif?imageView2/0/q/75|watermark/2/text/5YiY5aSn54i3/font/5a6L5L2T/fontsize/480/fill/IzAwMDAwMA==/dissolve/100/gravity/SouthEast/dx/10/dy/10|imageslim "自动效果")

## 元素选取
  单个元素选取Api：
  ```
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
```
 多个元素选取：
 ```
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
```
 另外还可以利用 By 类来确定哪种选择方式：
```
from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```

 By类的一些属性如下：
 ```
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```
这些方法跟JavaScript的一些方法有相似之处，find_element_by_id，就是根据标签的id属性查找元素，find_element_by_name，就是根据标签的name属性查找元素。举个简单的例子，比如我想找到下面这个元素：
```html
<input type="text" name="passwd" id="passwd-id" />
```
```python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_elements_by_tag_name("input")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
```


未完待续····
