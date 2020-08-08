from django.contrib import admin
from .models import Job , Category , Apply

# Register your models here.

admin.site.register(Job)
admin.site.register(Apply)
admin.site.register(Category)