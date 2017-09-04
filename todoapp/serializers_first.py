from rest_framework import serializers
from .models import *
class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoList
        fields=['name','createddate','user']

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=TodoItem
        fields=['name','description','completed_or_not','duedate','todolist']

