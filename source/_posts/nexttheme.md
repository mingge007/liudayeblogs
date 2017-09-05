---
title: 更换Next主题
date: 2017-08-18 17:54:31
tags:
- next
- hexo
- 博客
categories: 学习
#评论
comments: ture
#打赏
reward: true
toc: true
---
## 初衷
许久没有经营博客了，今天空闲下来，决定把遗留的问题统一解决一下
## 遗留问题
评论停服、yilia主题打赏体验太差、没有搜索功能、没有网站地图、没有订阅服务（RSS）、分类，标签不友好

## 选择Next主题
浏览自由博客大都使用Next主题，并且保持更新，文档清晰等优势，决定使用Next主题

### 安装Next主题
<!-- more -->

```shell
cd your-hexo-site
git clone https://github.com/iissnan/hexo-theme-next themes/next
```

### 使用Next主题

在站点配置文件（your-hexo-site/_config.yml）

```
theme: next
```
## Next主题详细设置

### 设置语言
在站点配置文件（your-hexo-site/_config.yml）

```
language: zh-Hans
```

在主题配置文件（your-hexo-site/themes/next/_config.yml）

```
language: zh-Hans
```

### 选择 Scheme
在主题配置文件（your-hexo-site/themes/next/_config.yml）

```
#scheme: Muse
#scheme: Mist
scheme: Pisces
#scheme: Gemini
```

### 设置 菜单
在主题配置文件（your-hexo-site/themes/next/_config.yml）

```
menu:
  home: /
  archives: /archives
  #about: /about
  categories: /categories
  tags: /tags
```

### 生成分类

```
cd your-hexo-site
hexo new page categories

```

### 编辑分类
your-hexo-site/source/categories/index.md

```
title: categories
date: 2017-08-18 13:37:50
type: "categories"
comments: false
```

### 生成标签

```
cd your-hexo-site
hexo new page tags

```
### 编辑标签
your-hexo-site/source/tags/index.md

```
title: tags
date: 2017-08-18 13:37:50
type: "tags"
comments: false
```

更多详细设置请查看[Next官方文档](http://theme-next.iissnan.com/theme-settings.html)

### 多说评论停止服务，网易云跟帖也停止服务 [hexo几种评论插件介绍](http://theme-next.iissnan.com/third-party-services.html)

最终选择了hyper评论插件[评论设置](https://www.hypercomments.com/documentation)

#### 设置hyper评论
在主题配置文件（your-hexo-site/themes/next/_config.yml）

```
menu:
hypercomments_id: **** //注册完，输入网站会给一串代码widget_id值就是该值
```

### 支持网站地图、RSS服务、搜索服务
在站点配置文件（your-hexo-site/_config.yml）

```
Plugins:
- hexo-generator-feed
- hexo-generator-sitemap
- hexo-generator-baidu-sitemap
```
### 安装网站地图插件

```shell
cd your-hexo-site
#安装sitemap
npm install hexo-generator-sitemap --save
#安装百度sitemap
npm install hexo-generator-baidu-sitemap --save
```

#### 设置配置文件
在站点配置文件（your-hexo-site/_config.yml）

```
sitemap:
  path: sitemap.xml
baidusitemap:
  path: baidusitemap.xml
```
部署完(hexo g)服务之后会在发布目录（public）生产两个文件baidusitemap.xml,sitemap.xml

### 安装feed插件

```
npm install hexo-generator-feed
```
#### 设置配置文件

在站点配置文件（your-hexo-site/_config.yml）

```
feed:
  type: atom       #feed 类型 (atom/rss2)
  path: atom.xml   #rss 路径
  limit: 20        #在 rss 中最多生成的文章数(0显示所有)
```
部署完(hexo g)服务之后会在发布目录（public）生产一个文件atom.xml

### 安装Local Search插件

```
npm install hexo-generator-searchdb --save
```
在站点配置文件（your-hexo-site/_config.yml）

```
search:
  path: search.xml
  field: post
  format: html
  limit: 10000
```

在主题配置文件（your-hexo-site/themes/next/_config.yml）

```
local_search:
  enable: true
```

#### 如果安装过插件可以执行更新指令

```
npm update 模块
```