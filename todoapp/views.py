# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from todoapp.models import *
from django.http import HttpResponse
from django.views.generic.edit import *
from django.urls import reverse_lazy
from todoapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers_first import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

def printlist(request):
    list_items=TodoList.objects.all()
    list_main_items=TodoItem.objects.all()
    return HttpResponse(list_main_items)
    template=loader.get_template('todoapp/todolist.html')
    context={
        'list_items':list_items,
        'list_main_items':list_main_items,
    }
    return HttpResponse(template.render(context,request))


def printlistlinks(request, id):

    list_main_items=TodoItem.objects.filter(list1_id=id)

    template = loader.get_template('todoapp/todoapplinks.html')
    context = {
        'list_main_items': list_main_items,
    }
    return HttpResponse(template.render(context, request))

def printtodohome(request):
    list_items=TodoList.objects.all()
    template=loader.get_template('todoapp/todohomepage.html')
    context={
        'list_items':list_items,
    }
    return HttpResponse(template.render(context, request))

class  createtodoitem(CreateView):
    model=TodoItem
    fields=['description','completed_or_not','duedate','list1']
    template_name='todoapp/todocreateitem.html'
    success_url=reverse_lazy('todoapp:todohome')


class updatetodoitem(UpdateView):
    model=TodoItem
    fields = ['description', 'completed_or_not', 'duedate', 'list1']
    template_name = 'todoapp/todoupdateitem.html'
    success_url = reverse_lazy('todoapp:todohome')

class deletetodoitem(DeleteView):
    model=TodoItem
    template_name = 'todoapp/todoapp_delete_full_item.html'
    success_url = reverse_lazy('todoapp:todohome')

class createtodolist(CreateView):
    model=TodoList
    fields=['name','createddate','user']
    template_name = 'todoapp/todocreatelist.html'
    success_url = reverse_lazy('todoapp:todohome')

class updatetodolist(UpdateView):
    model=TodoList
    fields = ['name', 'createddate']
    template_name = 'todoapp/todoupdatelist.html'
    success_url = reverse_lazy('todoapp:todohome')


class deletetodolist(DeleteView):
    model=TodoList
    template_name = 'todoapp/tododeletelist.html'
    success_url = reverse_lazy('todoapp:todohome')


class print_todolist_using_serializers(APIView):

    def get(self, request, format=None):
        id = request.user.id
        lists = TodoList.objects.filter(user_id=id)
        serializer = ToDoListSerializer(lists, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class print_todolist_using_id_serializers(APIView):


    def get(self, request,pk,format=None):

        try:
            id = request.user.id
            college_temp = TodoList.objects.filter(user_id=id).get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = ToDoListSerializer(college_temp)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        try:
            id = request.user.id
            college_temp = TodoList.objects.filter(user_id=id).get(pk=pk)
        except:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = ToDoListSerializer(college_temp, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        try:
            id = request.user.id
            college_temp = TodoList.objects.filter(user_id=id).get(pk=pk)
        except:
            return HttpResponse(status=404)
        college_temp.delete()
        return HttpResponse(status=204)



class print_todoitem_using_serializers(APIView):

    def get(self,request,format=None):
        id=request.user.id
        item_temp = TodoItem.objects.filter(todolist_id__user_id=id)
        serializer =TodoItemSerializer(item_temp,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class print_todoitem_using_id_serializers(APIView):
    def get(self, request,pk,format=None):

        try:
            id = request.user.id
            college_temp = TodoItem.objects.filter(id=id).get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = TodoItemSerializer(college_temp)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        try:
            id = request.user.id
            college_temp = TodoItem.objects.filter(id=id).get(pk=pk)
        except:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = TodoItemSerializer(college_temp, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        try:
            id = request.user.id
            college_temp = TodoItem.objects.filter(id=id).get(pk=pk)
        except:
            return HttpResponse(status=404)
        college_temp.delete()
        return HttpResponse(status=204)


def temporary(request):
    return render(request,'todoapp/getlist.html')
