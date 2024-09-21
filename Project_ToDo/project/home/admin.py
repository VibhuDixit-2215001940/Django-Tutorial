from django.contrib import admin
from .models import Todo
#admin pannel mere pass ek model hai feedback naam ka usse register kar dio ok 

admin.site.site_header = 'Todo Admin'

# admin.site.register(Todo)
@admin.register(Todo)
class Todo(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')