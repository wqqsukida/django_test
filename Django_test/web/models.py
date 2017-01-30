#!/usr/bin/env python
# coding:utf-8
#生成数据库表向migrations,再migrate
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    
    password=models.CharField(max_length=50) #创建字符串类型字段
    
    Gender=models.BooleanField(default=False) #创建布尔类型字段
    
    Age = models.IntegerField(default=30) #创建整型字段
    
    addr=models.TextField(default='XXXX') #创建文本类型字段
    
    CreateDate = models.DateTimeField(default='2017-01-19 16:44') #创建时间类型字段
    
    typeId = models.ForeignKey('UserType')  #创建该字段关联的外键（一对多）

class UserType(models.Model):
    name=models.CharField(max_length=50) 
    
    
    



class Group(models.Model):
    
    group_name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.group_name
    
class User(models.Model):
    
    user_name = models.CharField(max_length=50)
    
    user_info = models.TextField(default='userinfo')
    
    group_relation = models.ManyToManyField('Group')  #创建该字段关联的外键（多对多）
    
    def __unicode__(self):
        return self.user_name
    

class Asset(models.Model):   #自动更新时间auto_now;对表增删改查
    
    user_name = models.CharField(max_length=50)
    
    create_date = models.DateTimeField(auto_now_add=True)
    
    change_date = models.DateTimeField(auto_now=True)
    
    
    
        
    