from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^edit/(\d+)/$', views.edit_todo, name='edit_todo'),
    url(r'^create/$', views.create_todo, name='create_todo'),
    url(r'^details/(\d+)/$', views.todo_details, name='todo_details'),
    url(r'^changepass/$', views.change_password, name='change_password'),
]
