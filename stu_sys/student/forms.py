#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/11/0011 22:16
# @Author  : Hython.com
# @File    : forms.py
from __future__ import unicode_literals
from django import forms
from .models import Student


# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名', max_length=128)
#     sex = forms.CharField(label='性别', choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='职业', max_length=128)
#     email = forms.CharField(label='信箱', max_length=128)
#     sns = forms.CharField(label='SNS', max_length=128)
#     phone = forms.CharField(label='电话', max_length=128)

class StudentForm(forms.ModelForm):
    def clean_phone(self):
        """验证数字"""
        cleaned_data = self.cleaned_data['phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)

    def clean_sns(self):
        """验证数字"""
        cleaned_data = self.cleaned_data['sns']
        try: return int(cleaned_data)
        except ValueError:
            raise forms.ValidationError('必须填写数字！')

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession', 'email', 'sns', 'phone'
        )
