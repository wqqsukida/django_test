#!/usr/bin/env python
# coding:utf-8
'''自定义帮助方法simple_tag'''
from django import template
#from django.utils.safestring import mark_safe
#from django.template.base import resolve_variable, Node, TemplateSyntaxError
 
register = template.Library()
 
@register.simple_tag
def mymethod(v1):
    result = v1*1000  #获取到的值v1乘以1000再返回
    return result
''' 
@register.simple_tag
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
    return mark_safe(result)
'''