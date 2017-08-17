## Welcome Liudaye网站

# 视频页自动发布原理
通过执行python程序抓取最新的资源放到liudayeblogs/source/vip/table.html
同hexo编译并且发布到git@github.com:mingge007/lsof_java.git

# 创建博客
hexo new 博客名 
会在生成一个markdown文件liudayeblogs/source/_posts/

起始格式使用如下
---
title: 标题
date: 2017-08-17 16:42:02
tags:
- 标题1
- 标题3
- 标题3
categories: 目录1
#评论
comments: ture
#打赏
reward: true
toc: true
---


# 编译网站文件并且上传
sh createWWW.sh

# 从git拉取最新版本代码，并且提交本地代码到git 库
sh submitgit.sh

# 本地查看效果
sh view.sh

## hexo 常用命令说明
hexo clean //清理public下的文件
hexo g //编译文件
hexo d //发布上传git
hexo new blog //创建博客