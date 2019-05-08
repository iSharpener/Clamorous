import requests

APP_ID = 'wxd336a1cb1065e187'
APP_SECRET = '406916122b40f19bc9ea3665deac8fda'
REDIRECT_URI = 'http://wtage.cn/activity/pai'


def get_code():
    url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=' + APP_ID + '&redirect_uri=' + REDIRECT_URI + '&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect'
    res = requests.get(url)
    return res.status_code


def get_session_key(code):
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=' + APP_ID + '&secret=' + APP_SECRET + '&code=%s&grant_type=authorization_code' % (
        code)

    res = requests.get(url)
    json_data = res.json()
    # print(json_data)
    openid = json_data.get('openid', None)
    # session = json_data.get('session_key', None)
    if openid:
        return True, openid
    return False, None