#!/usr/bin/env python
# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    
    password=models.CharField(max_length=50) #创建字符串类型字
   
    addr=models.TextField(default='XXXX') #创建文本类型字段

    user_type = models.ForeignKey('UserType')  #创建该字段关联的外键（一对多）

class UserType(models.Model):
    name=models.CharField(max_length=50) 
    


class Group(models.Model):
    
    group_name = models.CharField(max_length=50)
    
    user = models.ManyToManyField('UserInfo')
'''   
class User(models.Model):
    
    user_name = models.CharField(max_length=50)
        
    group_relation = models.ManyToManyField('Group')  #创建该字段关联的外键（多对多）
'''    
    

class Asset(models.Model):   
    
    hostname = models.CharField(max_length=50)
    
    ip = models.CharField(max_length=50)
    
    user_group = models.ForeignKey('Group')