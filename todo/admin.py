from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
	list_display = ('content', 'owner', 'dateCreated', 'status', 'priority')
	search_fields = ['content']
	list_filter = ['owner', 'status', 'priority']

admin.site.register(Todo, TodoAdmin)

class TodoInline(admin.TabularInline):
	model = Todo
	can_delete = True
	verbose_name_plural = 'Todo list for this user:'

class UserAdmin(UserAdmin):
	inlines = [TodoInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)