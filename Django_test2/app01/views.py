#!/usr/bin/env python
# coding:utf-8
from django.shortcuts import redirect,render,render_to_response,HttpResponse
from models import Asset,Group,UserInfo,UserType

# Create your views here.
def register(request):
    '''
    t1 = UserType.objects.create(name='超级管理员')
    t2 = UserType.objects.create(name='普通管理员')
    
    u1 = UserInfo.objects.create(username='Elaine',password='wqq19870422',addr='Beijing',user_type=t1)
    u2 = UserInfo.objects.create(username='Dylan',password='wqq19870422',addr='Beijing',user_type=t2)
    
    g1 = Group.objects.create(group_name='用户组A')
    g1.user.add(u1)
    g2 = Group.objects.create(group_name='用户组B')
    g2.user.add(u1)
    '''
    return HttpResponse('注册成功')

    
    
def login(request):
    ret = {'status':''}
    if request.method == 'POST':
        user = request.POST.get('username',None)  #获取input标签里的username的值 None：获取不到不会报错
        pwd = request.POST.get('password',None)
        is_empty = all([user,pwd])
        if is_empty:       
            count = UserInfo.objects.filter(username=user,password=pwd).count() #获取数据库UserInfo里满足username=user,password=pwd的数据条数
            
            if count == 1:
                return redirect('/app01/index/')
            else:
                ret['status'] = '用户名或密码错误'
        else:
            ret['status'] = '用户名和密码不能为空'
    return render_to_response('login.html',ret)

def host(request):
    ret = {'status':'','data':None,'group':None}
    
    usergroup = Group.objects.all()
    ret['group'] = usergroup
    
    if request.method == 'POST':
        hostname = request.POST.get('hostname',None)
        ip = request.POST.get('ip',None)
        groupID = request.POST.get('group',None)
        
        is_empty = all([hostname,ip])
        if is_empty:
            groupObj = Group.objects.get(id=groupID)
            Asset.objects.create(hostname=hostname,ip=ip,user_group=groupObj)
        else:
            ret['status'] = '主机名和ip不能为空'   
            
    data = Asset.objects.all()
    ret['data'] = data
    
    obj = Asset.objects.filter(user_group__group_name='用户组A') #取到 Asset表里用户组为A的主机数据
    #等同于 sql:SELECT * FROM app01_asset LEFT JOIN app01_group ON app01_group.group_name = '用户组A'
    
    for item in obj:
        print item.hostname,item.ip,item.user_group.group_name,item.user_group.id
    
    return render_to_response('host.html',ret) 
    
def index(request):
    return HttpResponse('登录成功')