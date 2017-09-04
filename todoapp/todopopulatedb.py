from django.core.management.base import BaseCommand, CommandError
from todoapp.models import TodoList
from todoapp.models import TodoItem
import datetime
class Command(BaseCommand):

    def handle(self,*args,**options):
        lists=[]

        lists.append(TodoList(name="office work"))
        lists.append(TodoList(name="learning work"))
        lists.append(TodoList(name="application"))
        lists.append(TodoList(name="missionrnd"))
        lists.append(TodoList(name="hostelwork"))
        for i in lists:
            i.save()
            for j in range(5):
                TodoItem(description=i.name+str(j),duedate='2017-06-23',list=i).save()
