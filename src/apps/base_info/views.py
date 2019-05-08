from django.http import HttpResponse
from django.shortcuts import render


def get_base_info(request):
    
    return HttpResponse(u"你好")
    # return render(request, 'base_info/getinfo.html')