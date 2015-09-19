from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^userLogin/$', views.userLogin, name='userLogin'),
	url(r'^userLogout/$', views.userLogout, name='userLogout'),
	url(r'^register/$', views.userRegister, name='userRegister'),
	url(r'^edit/(\d+)/$', views.editTodo, name='editTodo'),
	url(r'^create/$', views.createTodo, name='createTodo'),
	url(r'^details/(\d+)/$', views.todoDetails, name='todoDetails'),
	url(r'^changepass/$', views.changePassword, name='changePassword'),
]