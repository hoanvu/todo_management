# Django core imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect

# Project imports
from .models import Todo
from .forms import DetailForm, NewTodoForm


@login_required(login_url='/accounts/login/')
def index(request):
    """Show login page if user is not logged in, otherwise show todo list for this user"""
    message = ''

    if request.user.is_authenticated():
        current_user = request.user
        todo_list = Todo.objects.filter(owner=current_user) \
            .order_by('status', '-priority', 'content')

        priorities = Todo._meta.get_field('priority').choices
        pdict = dict(priorities)

        stats = Todo._meta.get_field('status').choices
        sdict = dict(stats)

        new_todo_form = NewTodoForm()

        if not todo_list:
            message = 'You have no todo item.'

        return render(request, 'todo/todo_list.html', {
            'todo_list': todo_list,
            'message': message,
            'pdict': pdict,
            'sdict': sdict,
            'new_todo_form': new_todo_form,
        })

###################################################################################################


@login_required
def create_todo(request):
    """Create a new todo item"""

    if request.method == 'POST':
        current_user = request.user
        priority = request.POST['priority']
        content = request.POST['content']

        todo = Todo(owner=current_user, content=content, priority=priority)
        new_todo_form = NewTodoForm(request.POST, instance=todo)

        if new_todo_form.is_valid():
            new_todo_form.save()

            return HttpResponseRedirect('/todo/')

###################################################################################################


@login_required
def edit_todo(request, todo_id):
    """Edit an existing todo item"""

    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        detail_form = DetailForm(request.POST, instance=todo)

        if detail_form.is_valid():
            detail_form.save()
            return HttpResponseRedirect('/todo/')

###################################################################################################


@login_required
def todo_details(request, todo_id):
    """Show detail information for a todo item"""

    todo = Todo.objects.get(id=todo_id)
    priority_list = Todo._meta.get_field('priority').choices
    status_list = Todo._meta.get_field('status').choices
    detail_form = DetailForm(instance=todo)

    return render(request, 'todo/details.html', {
        'todo': todo,
        'priority_list': priority_list,
        'status_list': status_list,
        'detail_form': detail_form,
    })

###################################################################################################


# @login_required
# def change_password(request):
#     """Change user's password"""

#     message = ''

#     if request.method == 'POST':
#         current_user = request.user
#         change_pass_form = ChangePasswordForm(request.POST)

#         if change_pass_form.is_valid():
#             new_password = change_pass_form.cleaned_data['new_password']
#             re_password = change_pass_form.cleaned_data['re_password']
#             current_password = change_pass_form.cleaned_data['current_password']

#             if not check_password(current_password, current_user.password):
#                 message = "Current password is incorrect."
#             else:
#                 if new_password == re_password:
#                     current_user.set_password(new_password)
#                     current_user.save()
#                     message = 'Your password has been changed.'

#                     return render(request, 'todo/change_password_success.html', {
#                         'message': message
#                     })
#                 else:
#                     message = 'Passwords do not match.'
#     else:
#         change_pass_form = ChangePasswordForm()

#     return render(request, 'todo/change_password.html', {
#         'message': message,
#         'change_pass_form': change_pass_form,
#     })
