# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (0, '男'),
        (1, '女'),
        (2, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="Email")
    sns = models.CharField(max_length=128, verbose_name="SNS")
    phone = models.CharField(max_length=128, verbose_name="电话")
    line = models.CharField(max_length=128, null=True, verbose_name="LINE")
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="审核状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    # unicode py2 用
    def __unicode__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"
