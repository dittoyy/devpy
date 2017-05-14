# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from models import Blog
def index(request):
    blog_list=Blog.objects.all()
    # print blog_list
    return render_to_response('index.html',{'blogs':blog_list})
