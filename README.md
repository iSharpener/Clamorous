
# 项目描述
#### 项目名称：Clamorous  
#### 研究生培养信息系统是基于微信公众平台的研究生培养信息管理系统  
#### [项目地址](https://github.com/iSharpener/Clamorous)  
#### 项目第一负责人：魏昀琦  
--------------------------------
# 如何运行
+ **开发环境配置**
    Django 1.11.1 微信公众开发平台
    腾讯云服务器(服务器地址:123.207.152.82)
    python3.6
+ **项目目录结构** 
  ```
    ├── Readme.md                     // help
    └──src                            // 代码资源文件
        ├── apps                      // Django项目中的各个app
        │    ├── base_info            // 学生基本信息app 
        |    │       ├── static       // 静态文件（css）
        |    │       ├── templates    // 页面模版文件
        |    │       ├── _init_.py    // base_info app的初始化文件
        |    │       ├── admin.py     // base_info app的管理文件
        |    │       ├── models.py    // base_info app的数据模型
        |    │       ├── views.py     // base_info app的后台逻辑代码
        |    │       ├── apps.py      // base_info app的配置文件
        |    │       └── urls.py      // base_info app的url配置
        |    │       
        │    ├── get_activity_info    // 各种活动项目app
        |    │       ├── static       // 静态文件（css）
        |    │       ├── templates    // 页面模版文件
        |    │       ├── _init_.py    // get_activity_info app的初始化文件
        |    │       ├── admin.py     // get_activity_info app的管理文件
        |    │       ├── models.py    // get_activity_info app的数据模型
        |    │       ├── commen.py    // 后台管理平台的数据导入与导出功能
        |    │       ├── getopenid.py // openid的获取
        |    │       ├── views.py     // get_activity_info app的后台逻辑代码
        |    │       ├── apps.py      // get_activity_info app的配置文件
        |    │       └── urls.py      // get_activity_info app的url配置
        |    │       
        │    └── wechat               // 微信公众号后台开发app  
        |           ├── _init_.py     // wechat app的初始化文件
        |           ├── admin.py      // wechat app的管理文件
        |           ├── apps.py       // wechat app的配置文件
        |           ├── basic.py      // access token的获取及第三方页面连接的重定向
        |           ├── material.py   // 微信公众平台素材管理模块
        |           ├── menus.py      // 微信公众号自定义菜单
        |           ├── models.py     // wechat app的数据模型
        |           ├── receive.py    // 微信公众号消息接收
        |           ├── reply.py      // 微信公众号消息回复
        |           ├── views.py      // wechat app的后台逻辑代码
        |           ├── wechatApi.py  // 微信公众号openid获取公众号接口
        |           ├── wechatConfig.py//微信公众号openid获取公众号配置
        |           └── urls.py       // wechat app的url配置
        │                  
        ├── Clamorous  
        |       ├── _init_.py         // Django项目的初始化文件
        |       ├── setting.py        // Django项目的基本配置
        |       ├── urls.py           // url配置
        |       └── wsgi.py           // Django中的异步处理
        │
        └── manage.py                 // Django中的manage文件```
-----------------------------------------------------------------
# 业务介绍
+ **后台数据管理平台**
[后台数据管理平台地址](http://www.isharpen.cn:8080/admin/)
+ **各个面及描述**
姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

