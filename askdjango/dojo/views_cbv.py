from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse


class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_tempalte_string().format(name=name)
        return HttpResponse(html)
    
    def get_tempalte_string(self):
        return '''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스 메이커가 되어드리겠습니다.</p>
    <hr/>
    dojo/post_list1
    '''

post_list1 = PostListView1.as_view()
 
class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = PostListView2.as_view()

 
class PostListView3(View):
    def get(self, request):
        return JsonResponse({
        'message': '안녕 파이썬&장고',
        'item': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})


post_list3 = PostListView3.as_view()
 
class ExcelDownloadView(object):
    pass