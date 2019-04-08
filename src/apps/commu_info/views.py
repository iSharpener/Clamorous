from django.http import HttpResponse
from django.views.generic import View
from apps.commu_info.models import *
from apps.commu_info.util import json_response
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import hashlib

decorators = [csrf_exempt]

@method_decorator(decorators, name='dispatch')
class LoginView(View):

    model = UserOnlineInfo

    def init_md5(self,str):
        md5 = hashlib.md5(str)
        return md5.hexdigest()

    def get(self,requests):
        return JsonResponse(json_response(-1,'请求方式错误',data={}))
    def post(self, requests):
        self.online_info = UserOnlineInfo()
        telephone = requests.POST.get('telephone')
        commu_obj = CommuInformation.objects.filter(telephone_num=telephone).first()
        if commu_obj:
            online_obj = UserOnlineInfo.objects.filter(stu_id=commu_obj.stu_id).first()
            if online_obj.online_status == '1':
                return JsonResponse(json_response(-1,'已经在线了',data={}))
            if online_obj.online_status == '0':
                UserOnlineInfo.objects.filter(stu_id=commu_obj.stu_id).update(online_status='1')
                data = {'token': online_obj.token}
                return JsonResponse(json_response(1, '登录成功', data=data))
            self.online_info.stu_id = commu_obj.stu_id
            self.online_info.online_status = 1
            encoding_str = 'Clamorous' + commu_obj.stu_id + telephone
            token = self.init_md5(encoding_str.encode('utf8'))
            self.online_info.token = token
            self.online_info.save()
            data = {'token':token}
            return JsonResponse(json_response(1,'登录成功',data=data))
        else:
            return JsonResponse(json_response(-1,'没有对应学生，请修改手机号信息',data={}))

@method_decorator(decorators, name='dispatch')
class LogoutView(View):

    def post(self,requests):
        telephone = requests.POST.get('telephone')
        commu_obj = CommuInformation.objects.filter(telephone_num=telephone).first()
        if commu_obj:
            online_obj = UserOnlineInfo.objects.filter(stu_id=commu_obj.stu_id).first()
            if online_obj.online_status == '1':
                UserOnlineInfo.objects.filter(stu_id=commu_obj.stu_id).update(online_status='0')
                return JsonResponse(json_response(1, '下线成功', data={}))
            if online_obj.online_status == '0':
                return JsonResponse(json_response(-1,'已经是下线状态',data={}))
        else:
            return JsonResponse(json_response(-1,'没有对应学生，下线失败',data={}))


