# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "JiaSswee的Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2022-02-12T19:00+08:00"
author = "JiaSswee"
email = "jiashiwei678@gmail.com"
author_homepage = "https://www.829658.xyz"
description = "摸鱼中……"
key_words = ['Maverick', 'JiaSswee', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "JiaSswee的碎碎念",
        "url": "https://blog.829658.xyz",
        "brief": "JiaSswee的公开日记本"
    },
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "三無計劃",
        "url": "https://www.imalan.cn",
        "brief": "熊猫小A的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/JiaSswee",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/jiasswee",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/6613404686",
        "icon": "gi gi-weibo"
    },
    {
        "name": "Telegram",
        "url": "https://t.me/jiasswee",
        "icon": "gi gi-telegram"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
