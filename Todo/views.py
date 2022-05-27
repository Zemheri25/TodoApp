from unicodedata import name
from django.shortcuts import render, redirect
from .models import Todo
from .forms import Todo_Form



# Create your views here.


def home(request):
    return render(request, "Todo/home.html")

def Todo_List(request):
    todo = Todo.objects.all()
    context = {
        "todos":todo
    }

    return render(request, "Todo/todo_list.html", context)

def Todo_Create(request):
    form = Todo_Form()
    if request.method == "POST":
        form = Todo_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    
    
    context = {
        "form":form
    }

    return render(request, "Todo/todo_create.html", context)

def Todo_Update(request, id):
    todo = Todo.objects.get(id=id)
    form = Todo_Form(instance=todo)

    if request.method == "POST":
        form = Todo_Form(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        "form":form
    }

    return render(request, "Todo/todo_update.html", context)

def Todo_Delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("list")

    context = {
        "todo" : todo
    }

    return render(request, "Todo/todo_delete.html", context)


def Todo_Detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo":todo
    }

    return render(request, "Todo/todo_detail.html", context)



