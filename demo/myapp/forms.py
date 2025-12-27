from django import forms
from .models import ToDoItem,Course

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'completed']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)    

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description','content','img_url']