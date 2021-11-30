from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, ToDoItem
from .forms import CreateTodoList
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(response):    
    return render(response, "main/home.html",{})  #holds html template

def view1(response):
    return HttpResponse("<h1>View 1!</h>") #holds html

def todolist(response, id):
    #redirect if not authenticated or list doesn't belong to the user
    if (not response.user.is_authenticated):
        return redirect("/")
    try:
        ls = response.user.todolist_set.get(id=id)
    except ObjectDoesNotExist:
        return redirect("/")
    #ls = ToDoList.objects.get(id=id)

    if response.POST.get("save"):
        #print(response.POST)
        for item in ls.todoitem_set.all():
            if(response.POST.get("c"+str(item.id)) == "clicked"):
                item.complete = True
            else:
                item.complete = False
            itemText = response.POST.get("t"+str(item.id))
            if(itemText != item.text):
                item.text = itemText
            item.save()
    elif response.POST.get("addNewItem"):
        print(response.POST)
        text = response.POST.get("newItem")
        #since not using djangle form need to validate ourself
        if(len(text)<300 and len(text)>2):
            ls.todoitem_set.create(text=text, complete=False)
        else:
            print("Invalid todo item!")

    #items = ls.todoitem_set.get(id=1)
    #use template, pass dict (can use actual dict)
    return render(response, "main/todolist.html",{"todoList":ls}) 
   # return HttpResponse("<h1>%s</h1></br></br><p>%s</p>" % (ls.name,items.text))

def todolists(response):
    if(not response.user.is_authenticated):
        return redirect("/login")
    list = response.user.todolist_set.all()
    return render(response, "main/todolists.html",{"todoLists":list})

def createTodoList(response):
    #ensure user authenticated
    if(not response.user.is_authenticated):
        return redirect("/login")

    if response.method == "POST":
        form = CreateTodoList(response.POST)
        if(form.is_valid()):
            n = form.cleaned_data["name"]
            #the following breaks redirect
            #response.user.todolist_set.create(name=n)
            
            t=ToDoList(name = n, user=response.user)
            t.save()
            #response.user.todolist_set.add(t)
        #redirect
        return HttpResponseRedirect("/todolist/%i" %t.id)
    else:
        form = CreateTodoList()
    return render(response, "main/createTodoList.html",{"form":form})