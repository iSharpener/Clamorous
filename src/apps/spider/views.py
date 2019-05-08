from apps.commu_info.util import json_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.spider.models import *
from bs4 import BeautifulSoup
from .util import init_md5
from django.views.decorators.gzip import gzip_page

import json
import re
import requests as rq
import base64

#科研成果数据
@csrf_exempt
def get_research(requests):
    if requests.method=="POST":
        page = requests.POST.get('page')
        base_url = 'http://research.buct.edu.cn/zlcg/'
        if int(page) == 0:
            rq_url = 'http://research.buct.edu.cn/zlcg/index.htm'
        else:
            rq_url = 'http://research.buct.edu.cn/zlcg/index{}.htm'.format(page)
        resp = rq.get(rq_url)
        data = []
        try:
            soup_string = BeautifulSoup(resp.content, "html.parser")
            notice_list = soup_string.find(name='ul', class_='notice_list')
            lis = notice_list.find_all(name='li')
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '没有更多数据', data=data))
        i = 1
        for li in lis:
            item = {}
            span = li.find(name='span')
            item['id'] = i
            item['day'] = span.find(name='i').text.strip()
            alabel = li.find(name='a')
            item['style'] = alabel.find(name='span').text.strip()
            item['month'] = span.find(name='strong').text.strip()
            item['detail_url'] = base_url + alabel['href']
            alabel.span.decompose()
            item['content'] = alabel.text.strip()

            md5 = init_md5(item['detail_url'])
            result = ResearchInfo.objects.filter(md5=md5).first()
            if not result:
                obj = ResearchInfo(day=item['day'],style=item['style'],month=item['month'], \
                                   detail_url=item['detail_url'],content=item['content'],md5=md5)
                obj.save()
            else:
                item['day'] = result.day
                item['style'] = result.style
                item['month'] = result.month
                item['detail_url'] = result.detail_url
                item['content'] = result.content
            data.append(item)
            i += 1
        return JsonResponse(json_response(1, '成功', data=data))
    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))

#科研成果详情
def get_research_detail(requests):
    if requests.method=="GET":
        data = {}
        url = requests.GET.get('url','')
        try:
            resp = rq.get(url)
            soup_string = BeautifulSoup(resp.content.decode('utf8'), "html.parser")
            html = soup_string.find(name='div',class_='pageArticle article02')
            imgs = html.find_all(name='img')
            for img in imgs:
                img['src'] = img['src'].replace('../..','http://graduate.buct.edu.cn')
            data['html'] = str(html)
            return JsonResponse(json_response(1, '成功', data=data))
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '请求网页失败', data=data))
    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))

#校园招聘
@csrf_exempt
def zhaopin(requests):
    if requests.method=="POST":
        page = requests.POST.get('page')
        print(page)
        base_url = 'http://graduate.buct.edu.cn/jycy/xyzp/'
        if int(page) == 0:
            rq_url = 'http://graduate.buct.edu.cn/jycy/xyzp/index.htm'
        else:
            rq_url = 'http://graduate.buct.edu.cn/jycy/xyzp/index{}.htm'.format(page)
        headers = {
            'Connection': 'close'
        }
        resp = rq.get(rq_url, headers=headers)
        data = []
        soup_string = BeautifulSoup(resp.content.decode('utf8'), "html.parser")
        try:
            div_list = soup_string.find(name='div', class_='list02')
            lis = div_list.find(name='ul').find_all(name='li')
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '没有更多数据', data=data))
        i = 1
        for li in lis:
            date = li.find(name='span').text
            alabel = li.find(name='a')
            atext = alabel.text
            pattern = re.compile('【(.*?)】')
            result = re.search(pattern, atext)
            item = {}
            content = atext
            try:
                style = result.group(0)
                item['style'] = style
                content = atext.replace(style, '')
            except Exception as e:
                item['style'] = ''
            item['detail_url'] = base_url + alabel['href']
            item['id'] = i
            item['date'] = date
            item['content'] = content

            md5 = init_md5(item['detail_url'])
            result = CampusHireInfo.objects.filter(md5=md5).first()
            if not result:
                obj = CampusHireInfo(style=item['style'], date=item['date'], \
                                   detail_url=item['detail_url'], content=item['content'], md5=md5)
                obj.save()
            else:
                item['date'] = result.date
                item['style'] = result.style
                item['detail_url'] = result.detail_url
                item['content'] = result.content

            i += 1
            data.append(item)
        return JsonResponse(json_response(1, '成功', data=data))

    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))

#校园招聘详情
def zhaopin_detail(requests):
    if requests.method=="GET":
        data = {}
        url = requests.GET.get('url','')
        try:
            resp = rq.get(url)
            soup_string = BeautifulSoup(resp.content.decode('utf8'), "html.parser")
            html = soup_string.find(name='div',class_='right_con')
            imgs = html.find_all(name='img')
            for img in imgs:
                img['src'] = img['src'].replace('../..','http://graduate.buct.edu.cn')
            data['html'] = str(html)
            return JsonResponse(json_response(1, '成功', data=data))
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '请求网页失败', data=data))
    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))

#党建信息
@csrf_exempt
def dangjian(requests):
    if requests.method=="POST":
        page = requests.POST.get('page')
        print(page)
        base_url = 'http://graduate.buct.edu.cn/xsgz/dtjs/'
        if int(page) == 0:
            rq_url = 'http://graduate.buct.edu.cn/xsgz/dtjs/index.htm'
        else:
            rq_url = 'http://graduate.buct.edu.cn/xsgz/dtjs/index{}.htm'.format(page)
        headers = {
            'Connection': 'close'
        }
        resp = rq.get(rq_url, headers=headers)
        data = []
        soup_string = BeautifulSoup(resp.content.decode('utf8'), "html.parser")
        try:
            div_list = soup_string.find(name='div', class_='list02')
            lis = div_list.find(name='ul').find_all(name='li')
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '没有更多数据', data=data))
        i = 1
        for li in lis:
            date = li.find(name='span').text
            alabel = li.find(name='a')
            atext = alabel.text
            pattern = re.compile('【(.*?)】')
            result = re.search(pattern, atext)
            item = {}
            content = atext
            try:
                style = result.group(0)
                item['style'] = style
                content = atext.replace(style, '')
            except Exception as e:
                item['style'] = ''
            item['detail_url'] = base_url + alabel['href']
            item['id'] = i
            item['date'] = date
            item['content'] = content

            md5 = init_md5(item['detail_url'])
            result = PartyBuildingInfo.objects.filter(md5=md5).first()
            if not result:
                obj = PartyBuildingInfo(style=item['style'], date=item['date'], \
                                     detail_url=item['detail_url'], content=item['content'], md5=md5)
                obj.save()
            else:
                item['date'] = result.date
                item['style'] = result.style
                item['detail_url'] = result.detail_url
                item['content'] = result.content

            i += 1
            data.append(item)
        return JsonResponse(json_response(1, '成功', data=data))
    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))

#党建详情
def zhaopin_detail(requests):
    if requests.method=="GET":
        data = {}
        url = requests.GET.get('url','')
        try:
            resp = rq.get(url)
            soup_string = BeautifulSoup(resp.content.decode('utf8'), "html.parser")
            html = soup_string.find(name='div',class_='right_con')
            imgs = html.find_all(name='img')
            for img in imgs:
                img['src'] = img['src'].replace('../..','http://graduate.buct.edu.cn')
            data['html'] = str(html)
            return JsonResponse(json_response(1, '成功', data=data))
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '请求网页失败', data=data))
    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))

#就业指导信息
@csrf_exempt
def employment_counsel(requests):
    if requests.method=="POST":
        page = requests.POST.get('page')
        print(page)
        base_url = 'http://graduate.buct.edu.cn/jycy/jyzd/'
        if int(page) == 0:
            rq_url = 'http://graduate.buct.edu.cn/jycy/jyzd/index.htm'
        else:
            rq_url = 'http://graduate.buct.edu.cn/jycy/jyzd/index{}.htm'.format(page)
        headers = {
            'Connection': 'close'
        }
        resp = rq.get(rq_url, headers=headers)
        data = []
        soup_string = BeautifulSoup(resp.content.decode('utf8'), "html.parser")
        try:
            div_list = soup_string.find(name='div', class_='list02')
            lis = div_list.find(name='ul').find_all(name='li')
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '没有更多数据', data=data))
        i = 1
        for li in lis:
            date = li.find(name='span').text
            alabel = li.find(name='a')
            atext = alabel.text
            pattern = re.compile('【(.*?)】')
            result = re.search(pattern, atext)
            item = {}
            content = atext
            try:
                style = result.group(0)
                item['style'] = style
                content = atext.replace(style, '')
            except Exception as e:
                item['style'] = ''
            item['detail_url'] = base_url + alabel['href']
            item['id'] = i
            item['date'] = date
            item['content'] = content

            # md5 = init_md5(item['detail_url'])
            # result = PartyBuildingInfo.objects.filter(md5=md5).first()
            # if not result:
            #     obj = PartyBuildingInfo(style=item['style'], date=item['date'], \
            #                          detail_url=item['detail_url'], content=item['content'], md5=md5)
            #     obj.save()
            # else:
            #     item['date'] = result.date
            #     item['style'] = result.style
            #     item['detail_url'] = result.detail_url
            #     item['content'] = result.content

            i += 1
            data.append(item)
        return JsonResponse(json_response(1, '成功', data=data))
    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))

#就业指导详情
@gzip_page
def zhidao_detail(requests):
    if requests.method=="GET":
        data = {}
        url = requests.GET.get('url','')
        try:
            resp = rq.get(url)
            soup_string = BeautifulSoup(resp.content.decode('utf8'), "html.parser")
            html = soup_string.find(name='div',class_='right_con')
            imgs = html.find_all(name='img')
            for img in imgs:
                img['src'] = img['src'].replace('../..','http://graduate.buct.edu.cn')
            data['html'] = str(html)
            return JsonResponse(json_response(1, '成功', data=data))
        except Exception as e:
            print(e)
            return JsonResponse(json_response(-1, '请求网页失败', data=data))
    data = []
    return JsonResponse(json_response(-1, '请求方式有误', data=data))