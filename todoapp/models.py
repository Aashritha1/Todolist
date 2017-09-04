# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class TodoList(models.Model):
    name = models.CharField(max_length=128)
    createddate=models.DateField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    def __unicode__(self):
        return self.name


class TodoItem(models.Model):
    name = models.CharField(max_length=128)
    description=models.CharField(max_length=1024)
    completed_or_not=models.BooleanField(default=False)
    duedate=models.DateField(null=True, blank=True)
    todolist=models.ForeignKey(TodoList)

    def __unicode__(self):
        return self.description



# Create your models here.