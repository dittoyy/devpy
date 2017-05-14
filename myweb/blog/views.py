# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
from models import Blog

from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    blog_list=Blog.objects.all()
    # print blog_list
    return render_to_response('index.html',{'blogs':blog_list})
@csrf_exempt
# def login(request):
#     username = request.GET.get('username', '')
#     password = request.GET.get('password', '')
#     blog_list=Blog.objects.all()
#     if username == 'ditto' and password == '20112011pp':
#         return HttpResponse('login success!')
#     else:
#         return render_to_response('index.html',{'error':'username or password error!'})
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    blog_list=Blog.objects.all()
    # 判断用户名和密码不为空 
    if username != '' and password != '': 
        # return HttpResponse('login success!') 
        response = HttpResponseRedirect('/login_ok/') 
        response.set_cookie('username', username, 3600) 
        # 用户名 cookie 
        return response 
    else: 
        return render_to_response('index.html',{'error':'username or password error!', 'blogs':blog_list})

    # if username == 'ditto' and password == '20112011pp':
    #     return HttpResponse('login success!')
    # else:
    #     return render(request,'index.html',{'error':'username or password error!','blogs':blog_list})
# u'登录成功 '
def login_ok(request): 
    blog_list = Blog.objects.all() 
    username = request.COOKIES.get('username','') 
    # u'读取浏览器 cookie'
    return render_to_response('login_ok.html',{'user': username, 'blog_list': blog_list})
