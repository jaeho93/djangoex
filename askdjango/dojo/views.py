import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse

# Create your views here.
def mysum(request, numbers):
    # numbers = "1/2/3/14"
    result = map(lambda s: int(s or 0),numbers.split('/'))
    return HttpResponse(sum(result))


def hello(request, name, age):
    return HttpResponse("안녕하세요.{0}.{1}살이시네요.".format(name,age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스 메이커가 되어드리겠습니다.</p>
    <hr/>
    dojo/post_list1
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'item': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    # filepath = '/mnt/c/ubuntu/askdjango/basic/askdjango/dojo/aa.xls'
    filepath = os.path.join(settings.BASE_DIR, 'dojo/aa.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application.vnd.ms-excel')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
