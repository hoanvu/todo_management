from django import forms
from django.forms import ModelForm
from .models import Todo


# Todo detail form
class DetailForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['priority', 'status', 'moreinfo']
        widgets = {
            'moreinfo': forms.Textarea(attrs={'rows': 10}),
        }

        labels = {
            'moreinfo': 'More Information:',
        }


# New todo form
class NewTodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['content', 'priority']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 1, 'cols': 105})
        }
