from django.shortcuts import render
from .models import Todo

def todolist(request):
    alltodos=Todo.objects.all()
    return render(request,'todolist.html',{'alltodos':alltodos})