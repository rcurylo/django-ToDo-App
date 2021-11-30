from django import forms

class CreateTodoList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)