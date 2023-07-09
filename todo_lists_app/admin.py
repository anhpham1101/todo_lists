from django.contrib import admin
from todo_lists_app.models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
