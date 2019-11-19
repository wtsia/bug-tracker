from django.contrib import admin
from .models import Bugtracker

class BugtrackerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(Bugtracker, BugtrackerAdmin)