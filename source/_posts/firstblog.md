---
title: 博客安家手记
date: 2016-03-14 14:08:56
tags:
- 博客
- hexo
categories: 生活
#评论
comments: ture
#打赏
reward: true
toc: true
---
## 初心
每次看到大神们技术博客新颖清新，设计扁平，心中难免冲动就想拥有一个自己的博客，作为一个后端服务开发程序猿，一想到不熟悉的静态页面都会头大。
<!-- more -->
## 行动
域名申请下来已经两年了，忙到两年没有时间照顾自己了，年后终于找到些许时间决定调研一下，很快徜徉在各个前端大神清莲如润的博客当中，甚是惬意，像发现新大陆的孩童一般。很快chrome浏览器内存满为患，tab页已经无法数清。

## 选择
终于在简书当中发现一种正适合我的主站方式：[Github Pages](https://pages.github.com/) + [hexo](https://hexo.io/zh-cn/api/index.html) + 域名绑定；
教程：[参考教程:我的博客是如何搭建的（github pages + HEXO + 域名绑定） ](http://www.jianshu.com/p/834d7cc0668d),[手把手教你使用Hexo + Github Pages搭建个人独立博客](https://linghucong.js.org/2016/04/15/2016-04-15-hexo-github-pages-blog/)；
主题：[yilia](https://github.com/litten/hexo-theme-yilia)，这里有很多你想要的主题[可选主题列表](https://hexo.io/themes/)；
评论：[多说](http://duoshuo.com/)；
站长统计：[百度统计](http://tongji.baidu.com/web/welcome/login)；
访问统计：[不蒜子](http://ibruce.info/2015/04/04/busuanzi/)；

## 山路崎岖
难逃任何学习必经之路山路崎岖，只能慢行

### hexo d （发布到git）报错
{% codeblock lang:linux %}
hexo d
ERROR Deployer not found: git
{% endcodeblock %}
解决方法
{% codeblock lang:linux %}
npm install hexo-deployer-git –save
{% endcodeblock %}

### hexo发布覆盖git源代码，导致域名绑定CNAME消失
解决方法：在gitproject/source/下上传CNAME,以及其他静态费编译文件都可以放在这里

### 动态菜单显示异常
解决方法：

#### 安装插件
{% codeblock lang:linux %}
npm i hexo-generator-json-content --save
{% endcodeblock %}

#### 项目根配置_config.yml增加一下配置
{% codeblock %}
jsonContent:
    meta: false
    pages: false
    posts:
      title: true
      date: true
      path: true
      text: true
      raw: false
      content: false
      slug: false
      updated: false
      comments: false
      link: false
      permalink: false
      excerpt: false
      categories: false
      tags: true
{% endcodeblock %}

#### 评论插件安装
在主题（yilia）配置文件_config.yml中设置baidu_analytics，不是网站根配置文件

## 落户
www.liudaye.com