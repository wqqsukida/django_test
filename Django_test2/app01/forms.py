#!/usr/bin/env python
#_*_ coding:utf-8_*_

from django import forms

class ALogin(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)
    