from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from . import models

# Create your views here.
def home(request):
    todo_items=models.Todo.objects.all().order_by("-added_date")   
    return render(request, 'main/index.html',{
        "todo_items":todo_items
    })

def add_too(request):
    added_date = timezone.now()
    content=request.POST["search"]
    create=models.Todo.objects.create(added_date=added_date,text=content)
    length = models.Todo.objects.all().count()
    
    return HttpResponseRedirect('/')

def delete_todo(request,todo_id):
    print(todo_id)
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

def edit_todo(request,todo_id):
    todo_items=models.Todo.objects.all().order_by("-added_date")   
    mydictionary={
        "todo_items":todo_items
    }
    return render (request,'main/edit.html',context=mydictionary)


