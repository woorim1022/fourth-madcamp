from django.urls import path
from . import views

urlpatterns = [
    path('read/<int:letter_id>', views.read, name = 'read'), 
    path('write/', views.write, name = 'write'),
    path('reply/', views.reply, name='reply'),
    path('showlist/', views.showlist, name = 'showlist'),
]