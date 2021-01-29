from django import forms

class TaskCreationForm(forms.Form):
    taskName = forms.CharField(label='Task Name', max_length = 200)
    taskDescription = forms.CharField(label='Description', max_length = 1000)