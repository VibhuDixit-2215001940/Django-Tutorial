from django.contrib import admin
from .models import Feedback
from .models import Data
#admin pannel mere pass ek model hai feedback naam ka usse register kar dio ok 

admin.site.site_header = 'Vibhu Admin'

# admin.site.register(Feedback)
@admin.register(Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc')

# admin.site.register(Data)
@admin.register(Data)
class Data(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')