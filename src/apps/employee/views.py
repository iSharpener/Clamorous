from apps.commu_info.util import json_response
from django.http import HttpResponse, JsonResponse
from apps.employee.models import EmployeeInfo
import json

def get_job(requests):
    if requests.method=="GET":
        page = requests.GET.get('page',0)
        page = int(page)
        print('page:',page)
        if page < 0:
            return JsonResponse(json_response(-1,'页面参数错误',data={}))
        if page == 0:
            start_item = 0
            end_item = 10
        else:
            start_item = (page-1) * 10
            end_item = page * 10
    jobs = EmployeeInfo.objects.filter(id__gte=start_item).filter(id__lt=end_item)
    data = []
    for job in jobs:
        # 把Object对象转换成Dict对象
        dict = {
            'id':job.id,
            'company_name':job.company_name,
            'job_name':job.job_name,
            'address':job.address,
            'putdate':job.putdate,
            'responsibility':job.responsibility,
            'telephone':job.telephone,
            'qualification':job.qualification,
            'e_mail':job.e_mail,
            'remarks':job.remarks,
            'linkman':job.linkman,
        }
        data.append(dict)
    return JsonResponse(json_response(1, '成功', data=data))