from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view1/", views.view1, name="view 1"),
    path("todolist/<int:id>", views.todolist, name="todo list"),
    path("createtodolist/", views.createTodoList, name="create todo list"),
    path("todolists/",views.todolists,name="todo lists"),
    ]