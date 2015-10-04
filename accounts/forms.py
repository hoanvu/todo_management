from django import forms


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(label='Password:', widget=forms.PasswordInput())


# Register form
class RegisterForm(forms.Form):
    username = forms.CharField(label="Username:", max_length=100)
    email = forms.CharField(label="Email")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput())
    re_password = forms.CharField(label="Re-enter password:", widget=forms.PasswordInput())


# Change password form
class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label="Current password:", widget=forms.PasswordInput())
    new_password = forms.CharField(label="Enter new password:", widget=forms.PasswordInput())
    re_password = forms.CharField(label="Re-enter new password:", widget=forms.PasswordInput())
