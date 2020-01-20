from django.contrib import admin
from .models import Letter
from .models import Comment, Myhit, Emogi

# Register your models here.
admin.site.register(Letter)
admin.site.register(Comment)
admin.site.register(Emogi)
admin.site.register(Myhit)