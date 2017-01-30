#!/usr/bin/env python
#_*_ coding:utf-8_*_

from django import forms

class ALogin(forms.Form):
    username = forms.CharField(error_messages={'required':u'用户名不能为空','invalid':u'用户名格式错误'})
    
    email = forms.EmailField(
        error_messages={'required':u'邮箱不能为空','invalid':u'邮箱格式错误'},
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': u'邮箱'}) #为通过forms生成的html标签添加样式                   
                             )
    
    