# Django core imports
from django.shortcuts import render
from django.contrib.auth import login, authenticate, views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect, HttpResponse

# Project imports
from .models import Todo
from .forms import LoginForm, ChangePasswordForm, RegisterForm, DetailForm, NewTodoForm

def index(request):
	"""Show login page if user is not logged in, otherwise show todo list for this user"""
	message = ''

	if request.user.is_authenticated():
		currentUser = request.user
		todoList = Todo.objects.filter(owner=currentUser) \
									 .order_by('status', '-priority', 'content')
									 
		priorities = Todo._meta.get_field('priority').choices
		pdict = dict(priorities)

		stats = Todo._meta.get_field('status').choices
		sdict = dict(stats)

		new_todo_form = NewTodoForm()

		if not todoList:
			message = 'You have no todo item.'

		return render(request, 'todo/todoList.html', {
			'todoList': todoList,
			'message': message,
			'pdict': pdict,
			'sdict': sdict,
			'new_todo_form': new_todo_form,
		})
	else:
		return HttpResponseRedirect('/todo/userLogin/')

##########################################################################################################

def userLogin(request):
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

	return render(request, 'todo/login.html', {
		'login_form': login_form,
		'message': message,
	})

##########################################################################################################

# Log user out
@login_required
def userLogout(request):
	"""Log a user out"""
	return views.logout(request, next_page='/todo/', template_name='todo/login.html')

##########################################################################################################

# Register account
def userRegister(request):
	"""Register a new user"""

	message = ''

	if request.method == 'POST':
		register_form = RegisterForm(request.POST)

		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			email = register_form.cleaned_data['email']
			password = register_form.cleaned_data['password']
			re_password = register_form.cleaned_data['re_password']
			
			userList = User.objects.all()
			usernameList = [user.username for user in userList]
			emailList = [user.email for user in userList]

			# Check for a mountain of conditions 
			if username in usernameList:
				message = 'Username already taken.'
			elif not username:
				message = 'Username can not be empty.'
			elif email == '':
				message = 'Email is required.'
			elif email in emailList:
				message = 'Email already taken.'
			elif password != re_password:
				message = 'Passwords do not match.'
			else:
				newuser = User(username=username, email=email)
				newuser.set_password(password)
				newuser.save()
				return HttpResponseRedirect('/todo/')
	else:
		register_form	= RegisterForm()

	return render(request, 'todo/register.html', {
		'message': message,
		'register_form': register_form,
	})

##########################################################################################################

@login_required
def createTodo(request):
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

##########################################################################################################

@login_required
def editTodo(request, todoId):
	"""Edit an existing todo item"""

	if request.method == 'POST':
		todo = Todo.objects.get(id=todoId)
		detail_form = DetailForm(request.POST, instance=todo)

		if detail_form.is_valid():
			detail_form.save()
			return HttpResponseRedirect('/todo/')

##########################################################################################################

@login_required
def todoDetails(request, todoId):
	"""Show detail information for a todo item"""

	todo = Todo.objects.get(id=todoId)
	priorityList = Todo._meta.get_field('priority').choices
	statusList = Todo._meta.get_field('status').choices
	detail_form = DetailForm(instance=todo)

	return render(request, 'todo/details.html', {
		'todo': todo,
		'priorityList': priorityList,
		'statusList': statusList,
		'detail_form': detail_form,
	})

##########################################################################################################

@login_required
def changePassword(request):
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

					return render(request, 'todo/changePasswordSuccess.html', {
						'message': message
					})
				else:
					message = 'Passwords do not match.'
	else:
		change_pass_form = ChangePasswordForm()
		
	return render(request, 'todo/changePassword.html', {
		'message': message,
		'change_pass_form': change_pass_form,
	})
