from django.http import HttpResponse

def get_base_info(request):

    return HttpResponse(u"你好")