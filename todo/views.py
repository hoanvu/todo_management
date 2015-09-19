from django.shortcuts import render
from django.contrib.auth import login, authenticate, views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect, HttpResponse
from .models import Todo

# If user is not logged in, show login form
# Otherwise, show all todo items for this user
def index(request):
	message = ''

	if request.user.is_authenticated():
		currentUser = request.user
		todoList = Todo.objects.filter(owner=currentUser) \
									 .order_by('status', '-priority', 'content')
									 
		priorities = Todo._meta.get_field('priority').choices
		pdict = dict(priorities)

		stats = Todo._meta.get_field('status').choices
		sdict = dict(stats)

		if not todoList:
			message = 'You have no todo item.'

		return render(request, 'todo/todoList.html', {
			'todoList': todoList,
			'message': message,
			'pdict': pdict,
			'sdict': sdict,
		})
	else:
		return render(request, 'todo/login.html')

##########################################################################################################

# Log user in
def userLogin(request):
	message = ''
	if request.method == 'POST':
		username = request.POST.get('username').strip()
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/todo/')
			else:
				message = 'Account is disabled.'
		else:
			message = 'Incorrect username/password.'

	return render(request, 'todo/login.html', {'message': message})

##########################################################################################################

# Log user out
@login_required
def userLogout(request):
	return views.logout(request, next_page='/todo/', template_name='todo/login.html')

##########################################################################################################

# Register account
def userRegister(request):
	message = ''

	if request.method == 'POST':
		username = request.POST.get('username').strip()
		email = request.POST.get('email').strip()
		password = request.POST.get('password')
		repassword = request.POST.get('repassword')
		
		userList = User.objects.all()
		usernameList = [user.username for user in userList]
		emailList = [user.email for user in userList]

		# Check for a mountain of conditions 
		if username in usernameList:
			message = 'Username already taken.'
		elif not username:
			message = 'Username can not be empty.'
		elif email in emailList and email != '':
			message = 'Email already taken.'
		elif password != repassword:
			message = 'Passwords do not match.'
		else:
			newuser = User(username=username, email=email)
			newuser.set_password(password)
			newuser.save()
			return HttpResponseRedirect('/todo/')

	return render(request, 'todo/register.html', {'message': message})

##########################################################################################################

@login_required
def createTodo(request):
	if request.method == 'POST':
		currentUser = request.user
		content = request.POST.get('content')
		priority = request.POST['priority']

		# Because priority stored as Integer in database, value we get from <select>
		# will need to be converted back to integer
		priority = ['Low', 'Medium', 'High'].index(priority)

		newtodo = Todo(owner=currentUser, content=content, priority=priority)
		newtodo.save()

		return HttpResponseRedirect('/todo/')

##########################################################################################################

@login_required
def editTodo(request, todoId):
	if request.method == 'POST':
		priorityList = Todo._meta.get_field('priority').choices
		statusList = Todo._meta.get_field('status').choices

		priority1 = request.POST['priority']
		status1 = request.POST['status']
		moreinfo = request.POST.get('moreinfo')

		todo = Todo.objects.get(id=todoId)
		todo.moreinfo = moreinfo
		
		for item in priorityList:
			if item[1] == priority1:
				todo.priority = item[0]

		for item in statusList:
			if item[1] == status1:
				todo.status = item[0]

		todo.save()

		return HttpResponseRedirect('/todo/')

##########################################################################################################

@login_required
def todoDetails(request, todoId):
	todo = Todo.objects.get(id=todoId)
	priorityList = Todo._meta.get_field('priority').choices
	statusList = Todo._meta.get_field('status').choices
	return render(request, 'todo/details.html', {
		'todo': todo,
		'priorityList': priorityList,
		'statusList': statusList,
	})

##########################################################################################################

@login_required
def changePassword(request):
	message = ''

	if request.method == 'POST':
		currentUser = request.user
		password = request.POST.get('password')
		repassword = request.POST.get('repassword')
		currPassword = request.POST.get('currPassword')

		if not check_password(currPassword, currentUser.password):
			message = "Current password is incorrect."
		else:
			if password == repassword:
				currentUser.set_password(password)
				currentUser.save()
				message = 'Your password has been changed.'

				return render(request, 'todo/changePasswordSuccess.html', {
					'message': message
				})
			else:
				message = 'Passwords do not match.'

	return render(request, 'todo/changePassword.html', {
		'message': message
	})
