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
from django.contrib import auth
from django.contrib.auth.decorators import login_required

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
    
    # # cookie和session判断用户名和密码不为空 
    # if username != '' and password != '': 
    #     # return HttpResponse('login success!') 
    #     response = HttpResponseRedirect('/login_ok/') 
    #     # response.set_cookie('username', username, 3600) # 用户名 cookie 
    #     request.session['username']=username # 将 session 信息写到服务器 
    #     return response 
    # else: 
    #     return render_to_response('index.html',{'error':'username or password error!', 'blogs':blog_list})

    # # if username == 'ditto' and password == '20112011pp':
    # #     return HttpResponse('login success!')
    # # else:
    # #     return render(request,'index.html',{'error':'username or password error!','blogs':blog_list})

    #关窗不允许直接log_ok页面空登陆
    users_=[username]
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)#验证登录
        response=HttpResponseRedirect('/login_ok/')
        request.session['username']=users_
        return response
    else:
        return render_to_response('index.html',{'error':'username or password error!', 'blogs':blog_list})



# u'登录成功 '
@login_required
def login_ok(request): 
    blog_list = Blog.objects.all() 
    # username = request.COOKIES.get('username','') # u'读取浏览器 cookie'
    username = request.session.get('username', '') # 读取用户 session
    user=username[0]
    return render_to_response('login_ok.html',{'user': username, 'blog_list': blog_list})
# 退出登录 
@login_required
def logout(request): 
    response = HttpResponseRedirect('/index/') 
    # u'返回首页 ''
    # response.delete_cookie('username') # u'清理 cookie 里保存 username ''
    del request.session['username']# 清理用户 session
    return response
