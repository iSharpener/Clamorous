# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
from basic import Basic


class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":[
        {
            "name": "培养信息",
            "sub_button":
            [
                {
                    "type": "view",
                    "name": "活动速递",
                    "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=1&sn=1e89c8f21a03235171ec6d162d250c54"
                },
                {
                    "type": "view",
                    "name": "公示",
                    "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=3&sn=39b761461d0245c7bf87fb2d44d25846"
                },
                {
                    "type":"view",
                    "name":"科技生活",
                    "url":"https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=4&sn=02f2b4aa5bab342e02b6c54a95636918"	
                },
                {
                    "type":"view",
                    "name":"研究生院官网",
                    "url":"http://graduate.buct.edu.cn/"	
                }
            ]
        },
	    {
            "name": "我", 
            "sub_button": 
            [
                {
                    "type": "view", 
                    "name": "已参加活动", 
                    "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxd336a1cb1065e187&redirect_uri=http://wtage.cn/activity/pai&response_type=code&scope=snsapi_base&state=STATE"
                }, 

                {
                    "type": "view", 
                    "name": "指南", 
                    "url": "http://wtage.cn/activity/help"
                }
            ]
	    },
	    ]
    }
    """

                # {
                #     "type": "view", 
                #     "name": "我的培养计划", 
                #     "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzU2ODgzNDU0MQ==&hid=1&sn=1e89c8f21a03235171ec6d162d250c54"
                # },
    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
