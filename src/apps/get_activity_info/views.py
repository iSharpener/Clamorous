from django.http import HttpResponse
from django.shortcuts import render
from apps.get_activity_info.models import SignUpInfo, ParticipationRecord, MoralActivity, AcademicReport
from apps.base_info.models import BaseInformation, BindWechat
import hashlib
import time
from apps.wechat.receive import parse_xml
from apps.wechat import receive, reply
from apps.get_activity_info.getopenid import get_session_key, get_code


def post_activity_info(request):

    if request.method == 'GET':
        # print(1)
        code = request.GET.get('code')
        # print(code)
        # if code is None:
        #     print(2)
        #     code = get_code()
        #     print(code)
        flag, openid = get_session_key(code)
        # print(openid)
        if flag:
            bindwechardata = BindWechat.objects.filter(
                stu_openid=openid).values()
            stuid = bindwechardata[0]['stu_id']
            list1 = ParticipationRecord.objects.filter(stu_id=stuid).values()
            list2 = MoralActivity.objects.filter(stu_id=stuid).values()
            list3 = AcademicReport.objects.filter(stu_id=stuid).values()
            context = {"list1": list1, "list2": list2, "list3": list3}
            # return HttpResponse(list1)
            # return HttpResponse(webData)
            return render(request, 'get_activity_info/showinfo.html', context)
            # return render(request, 'get_activity_info/warn_showinfo.html')
            # print(stuid)
        else:
            return render(request, 'get_activity_info/warn_showinfo.html')

    return render(request, 'get_activity_info/showinfo.html')


def get_activity_info(request, name, time):
    act_name = name
    act_time = time
    context = {"act_name": act_name, "act_time": act_time}
    return render(request, 'get_activity_info/getinfo.html', context)


def activity(request):
    return render(request, 'get_activity_info/activity.html')


def data_post(request):
    if request.method == "POST":
        # 获得报名人员的信息
        stu_name = request.POST.get('stu_name')
        stu_id = request.POST.get('stu_id')
        stu_class = request.POST.get('stu_class')
        act_name = request.POST.get('act_name')
        act_time = request.POST.get('act_time')
        stu_status = request.POST.get('stu_status')

        # 在人员信息表中查找是否有这个报名的人
        base_info_stu_id = BaseInformation.objects.values_list(
            'stu_id', flat=True)
        base_info_stu_name = BaseInformation.objects.values_list(
            'stu_name', flat=True)
        base_info_stu_class = BaseInformation.objects.values_list(
            'stu_class', flat=True)

        if stu_id in base_info_stu_id and stu_name in base_info_stu_name and stu_class in base_info_stu_class:
            # 如果存在这个报名的人，则查找是否已经报名
            data = SignUpInfo.objects.filter(stu_id=stu_id).values_list(
                'stu_id', 'act_name', 'stu_status', 'id')
            # print(data)
            d_dict = {}
            for i in data:
                d_dict[i[:3]] = i[-1]

            if (stu_id, act_name, stu_status) in d_dict.keys():
                # 若已经存在报名信息，则返回已经报名页面，提示用户切勿重复报名！
                return render(request, 'get_activity_info/warn_getinfo.html')

            else:
                # 若没有报过名，则提交数据进入数据库，返回报名成果页面
                signup = SignUpInfo()
                signup.stu_name = stu_name
                signup.stu_id = stu_id
                signup.stu_class = stu_class
                signup.act_name = act_name
                signup.act_time = act_time
                signup.stu_status = stu_status
                signup.save()
                return render(request, 'get_activity_info/success.html')

        else:
            return render(request, 'get_activity_info/warn.html')


def get_help_info(request):
    return render(request, 'get_activity_info/help.html')


def test(request):
    av_catalog = {
        'list1': [{
            'act_name': '新生教育',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2018-09'
        }, {
            'act_name': '校庆活动',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-01'
        }, {
            'act_name': '雄安新区汇报',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-03'
        }],
        'list2': [{
            'act_name': '新生教育',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2018-09'
        }, {
            'act_name': '校庆活动',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-01'
        }, {
            'act_name': '雄安新区汇报',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'status': '参与人员',
            'act_time': '2019-03'
        }],
        'list3': [{
            'act_name': '新生教育',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'act_time': '2018-09'
        }, {
            'act_name': '校庆活动',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'act_time': '2019-01'
        }, {
            'act_name': '雄安新区汇报',
            'stu_name': '赵宇',
            'stu_id': '2018200696',
            'act_time': '2019-03'
        }]
    }
    return render(request, 'get_activity_info/help.html')
