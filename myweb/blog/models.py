# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.

class Blog(models.Model):
    """docstring for Blog"""
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()

    # def __init__(self, arg):
    #     super(Blog, self).__init__()
    #     self.arg = arg

class BlogAdmin(admin.ModelAdmin):
        """docstring for BlogAdmin"""
        # def __init__(self, arg):
        #     super(BlogAdmin, self).__init__()
        #     self.arg = arg
        list_display=('title','timestamp')

admin.site.register(Blog,BlogAdmin)
                