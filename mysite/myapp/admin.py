from django.contrib import admin
from .models import Letter
from .models import Comment

# Register your models here.
admin.site.register(Letter)
admin.site.register(Comment)