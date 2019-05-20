from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from apps.wechat.models import BindWechat
from apps.base_info.models import BaseInformation
import hashlib
import time
from apps.wechat.receive import parse_xml
from apps.wechat import receive, reply
from django.db.models import Q


@csrf_exempt
def weixin_main(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'wtage'

        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print('[token, timestamp, nonce]', hashlist)
        hashstr = ''.join([s for s in hashlist]).encode(
            'utf-8')  #这里必须增加encode('utf-8'),否则会报错
        print('hashstr befor sha1', hashstr)
        hashstr = hashlib.sha1(hashstr).hexdigest()
        print('hashstr sha1', hashstr)
        if hashstr == signature:
            return HttpResponse(echostr)  #必须返回echostr
        else:
            return HttpResponse('error')  #可根据实际需要返回
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)


def autoreply(request):
    try:
        webData = str(request.body, encoding='utf-8')
        print("Handle Post webdata is ", webData)
        recMsg = parse_xml(webData)
        if isinstance(recMsg, receive.Msg):
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.MsgType == 'text':
                if recMsg.Content == '绑定':
                    content = '请输入：“绑定+学号”，例如：绑定+2019000111'
                elif recMsg.Content[0:3] == '绑定+':

                    temp = recMsg.Content[3:]
                    data = BaseInformation.objects.filter(stu_id=temp).values()

                    # print(data)
                    if len(data) != 0:
                        # print(len(data))
                        # if data is None:
                        #     print(123)
                        bdata = BindWechat.objects.filter(
                            Q(stu_id=temp) | Q(stu_openid=toUser)).values()
                        # print(bdata)
                        if bdata.exists():
                            content = "当前微信号或学号已被绑定，如有疑问请联系管理员！"
                        else:
                            # print(data[0]['stu_id'])
                            binddata = BindWechat()
                            binddata.stu_id = data[0]['stu_id']
                            binddata.stu_name = data[0]['stu_name']
                            binddata.stu_class = data[0]['stu_class']
                            binddata.stu_openid = toUser
                            binddata.save()
                            content = "绑定成功!"
                    else:

                        content = "学号不存在！请重新输入"
                else:
                    # print(recMsg.Content)
                    print(2)
                    content = recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            if recMsg.MsgType == 'image':
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
        if isinstance(recMsg, receive.EventMsg):
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.Event == 'subscribe':
                content = "感谢您关注【研究生培养信息系统】\n回复:“绑定”查看绑定详情！\n更多内容，敬请期待..."
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            if recMsg.Event == 'VIEW':
                content = "点击VIEW"
                # print(toUser)
                # print(fromUser)
                # print(content)
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            if recMsg.Event == 'CLICK':
                # if recMsg.Eventkey == 'Help':
                content = "编写中，尚未完成"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
        else:
            return "success"
            print("暂且不处理")
        # return Msg().send()
    except (Exception) as Argment:
        return Argment


# from django.views.generic import View
# from django.http import HttpResponseRedirect
# from django.http import HttpResponse, HttpResponseServerError
# from django.shortcuts import render, redirect
# from apps.wechat.WechatAPI import WechatLogin

# class WechatViewSet(View):
#     wechat_api = WechatLogin()

# class AuthView(WechatViewSet):
#     def get(self, request):
#         url = self.wechat_api.get_code_url()
#         return redirect(url)

# class GetInfoView(WechatViewSet):
#     def get(self, request):
#         if 'code' in request.GET:
#             code = request.GET['code']
#             token, openid = self.wechat_api.get_access_token(code)
#             if token is None or openid is None:
#                 return HttpResponseServerError('get code error')
#             user_info, error = self.wechat_api.get_user_info(token, openid)
#             if error:
#                 return HttpResponseServerError('get access_token error')
#             user_data = {
#                 'nickname': user_info['nickname'],
#                 'sex': user_info['sex'],
#                 'province': user_info['province'].encode('iso8859-1').decode('utf-8'),
#                 'city': user_info['city'].encode('iso8859-1').decode('utf-8'),
#                 'country': user_info['country'].encode('iso8859-1').decode('utf-8'),
#                 'avatar': user_info['headimgurl'],
#                 'openid': user_info['openid']
#             }
#             user = BeautyUsers.objects.filter(is_effective=True).filter(wechat=user_data['openid'])
#             if user.count() == 0:
#                 user = BeautyUsers.objects.create(username=user_data['nickname'],
#                                                   wechat_avatar=user_data['avatar'],
#                                                   wechat=user_data['openid'],
#                                                   password='')
#                 login(request, user)
#             else:
#                 login(request, user.first())
#             # 授权登录成功，进入主页
#             return home(request)
