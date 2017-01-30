#!/usr/bin/env python
# coding:utf-8
#对数据库表进行操作：增删改查
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from models import Asset,UserInfo,User,Group  #导入models里的Asset（表）类
from django.shortcuts import render_to_response
from django.template.context_processors import request
# Create your views here.

def add(requset,name):
    Asset.objects.create(user_name=name)  #对表Asset增加一条数据
    '''
    add_obj = Asset(user_name=name)
    add_obj.save()
    '''
    return  HttpResponse('ok')

def delete(requset,name):
    '''
    Asset.objects.get(user_name=name).delete() #获取user_name=name的数据,然后删除    
    '''
    Asset.objects.filter(user_name__icontains=name).delete() #获取user_name包含name的数据,然后删除
    #get和filter的区别，get获取不到数据会报错，filter则不会
    return  HttpResponse('ok')
def update(requset,id,name):
    '''
    obj_update = Asset.objects.get(id=id) #获取user_id=id的数据
    obj_update.user_name = name #让该列的user_name字段等于name
    obj_update.save() #保存
    '''
    Asset.objects.filter(id__gt=id).update(user_name=name) #过滤获取id>id的数据，并让其username=name
    return  HttpResponse('ok')
    
    
def get(requset,name):
    '''
    list = Asset.objects.filter(user_name__contains=name) #过滤获取user_name包含name的数据
    for item in list:
        print item.id
    '''
    all_data = Asset.objects.all() #获取所有数据
    print all_data.query #打印该条的sql语句
    list = Asset.objects.all()[0:2] #获取从0-2条数据
    all_data = Asset.objects.all().order_by('-id') #按id从大到小排序获取到的数据
    #all_data = Asset.objects.all().values('id','user_name',) #获取所有数据中的id和user_name两列
    print all_data
        
    return  HttpResponse('ok')

def Many(request):
    u1 = User.objects.get(id=1)
    g1 = Group.objects.get(id=1)
    u_all = User.objects.all()
    g_all = Group.objects.all()
    
    #u1.group_relation.add(g1)  #向多对多表里添加一条数据（多对多关系）
    #u1.group_relation.remove(g1) #向多对多表里删除一条数据
    #print u1.group_relation.all().filter(group_name = 'couple')
    
    
    return HttpResponse('ok')

def Assetlist(requset):
    asset_list = Asset.objects.all() #获取数据库里的数据
    
    result = render_to_response('assetlist.html',{'data':asset_list,'user':'Elaine'})
    #返回assetlist.html并将定义的字典data数据传给html文件
    return result

def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)  #获取input标签里的username的值 None：获取不到不会报错
        pwd = request.POST.get('password',None)
        '''
        print user,pwd
        return render_to_response('login.html')
        '''
        result = UserInfo.objects.filter(username=user,password=pwd).count() #获取数据库UserInfo里满足username=user,password=pwd的数据条数
        if result == 1:
            return HttpResponse('登录成功')
        else:
            return render_to_response('login.html',{'status':'用户名密码错误'}) #返回login.html,并将status字典传给html文件
    else:
        return render_to_response('login.html')
        
    
      
