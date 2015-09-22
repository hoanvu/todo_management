from django import forms
from django.forms import ModelForm	
from .models import Todo

# Login form
class LoginForm(forms.Form):
	username = forms.CharField(label='Username:', max_length=100)
	password = forms.CharField(label='Password:', widget=forms.PasswordInput())

# Change password form
class ChangePasswordForm(forms.Form):
	current_password = forms.CharField(label="Current password:", widget=forms.PasswordInput())
	new_password = forms.CharField(label="Enter new password:", widget=forms.PasswordInput())
	re_password = forms.CharField(label="Re-enter new password:", widget=forms.PasswordInput())

# User register form
class RegisterForm(forms.Form):
	username = forms.CharField(label="Username:", max_length=100)
	email = forms.CharField(label="Email")
	password = forms.CharField(label="Password:", widget=forms.PasswordInput())
	re_password = forms.CharField(label="Re-enter password:", widget=forms.PasswordInput())

# Todo detail form
class DetailForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['priority', 'status', 'moreinfo']
		widgets = {
			'moreinfo': forms.Textarea(attrs={ 'rows': 10 }),
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
			'content': forms.Textarea(attrs={ 'rows': 1, 'cols': 105 })
		}