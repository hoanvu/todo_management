from django.shortcuts import render
from django.contrib.auth import authenticate, login, views
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from .forms import LoginForm, RegisterForm, ChangePasswordForm


def user_login(request):
    """Log user in"""
    message = ''
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        # if form data is valid
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            # if user is authenticated successfully
            if user is not None:
                # and the account is active
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/todo/')
                else:
                    message = 'Account is disabled.'
            else:
                message = 'Incorrect username or password.'

    else:
        login_form = LoginForm()

    return render(request, 'accounts/login.html', {
        'login_form': login_form,
        'message': message,
    })


@login_required
def user_logout(request):
    """Log a user out"""
    return views.logout(request, next_page='/todo/', template_name='accounts/login.html')


def user_register(request):
    """Register a new user"""

    message = ''

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            re_password = register_form.cleaned_data['re_password']

            user_list = User.objects.all()
            username_list = [user.username for user in user_list]
            email_list = [user.email for user in user_list]

            # Check for a mountain of conditions
            if username in username_list:
                message = 'Username already taken.'
            elif not username:
                message = 'Username can not be empty.'
            elif email == '':
                message = 'Email is required.'
            elif email in email_list:
                message = 'Email already taken.'
            elif password != re_password:
                message = 'Passwords do not match.'
            else:
                newuser = User(username=username, email=email)
                newuser.set_password(password)
                newuser.save()
                return HttpResponseRedirect('/todo/')
    else:
        register_form = RegisterForm()

    return render(request, 'accounts/register.html', {
        'message': message,
        'register_form': register_form,
    })


@login_required
def change_password(request):
    """Change user's password"""

    message = ''

    if request.method == 'POST':
        current_user = request.user
        change_pass_form = ChangePasswordForm(request.POST)

        if change_pass_form.is_valid():
            new_password = change_pass_form.cleaned_data['new_password']
            re_password = change_pass_form.cleaned_data['re_password']
            current_password = change_pass_form.cleaned_data['current_password']

            if not check_password(current_password, current_user.password):
                message = "Current password is incorrect."
            else:
                if new_password == re_password:
                    current_user.set_password(new_password)
                    current_user.save()
                    message = 'Your password has been changed.'

                    return render(request, 'accounts/change_password_success.html', {
                        'message': message
                    })
                else:
                    message = 'Passwords do not match.'
    else:
        change_pass_form = ChangePasswordForm()

    return render(request, 'accounts/change_password.html', {
        'message': message,
        'change_pass_form': change_pass_form,
    })
