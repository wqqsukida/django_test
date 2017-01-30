#!/usr/bin/env python
#_*_ coding:utf-8_*_

from django.shortcuts import render,render_to_response
import json
# Create your views here.
from forms import ALogin
from django.http.response import HttpResponse

def index(request):
    ret = {'data':'','error':''}
    obj = ALogin()
    ret['data'] = obj 
    
    if request.method == 'POST':         
        checkForm = ALogin(request.POST)
        checkResult = checkForm.is_valid() #检查从html返回的值是否为True(格式正确，非空）
        if checkResult: #如果返回值为True，则pass
            pass
        else: #返回值False,附加错误信息，并返回用户输入的checkForm
            #print checkForm.errors
            #print type(checkForm.errors) #<class 'django.forms.utils.ErrorDict'>            
            #errorObj = checkForm.errors #返回一个对象类型的错误信息
            FristErrorMsg = checkForm.errors.as_data().values()[0][0].messages[0] #返回一条字符串类型的错误信息
            
            ret['data'] = checkForm
            ret['error'] = FristErrorMsg
            return render_to_response('app03/index.html',ret)
    return render_to_response('app03/index.html',ret)

def Ajax(request):
    if request.method == 'POST':
        print request.POST
        data = {'status':0,'msg':'请求成功','data':[1,2,3,4]}
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('app03/ajax.html',)    
        