from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]
