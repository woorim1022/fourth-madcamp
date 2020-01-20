from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:letter_id>', views.detail, name = 'detail'), 
    path('write/', views.write, name = 'write'),
    path('reply/', views.reply, name='reply'),
    path('showlist/', views.showlist, name = 'showlist'),
    path('lettercreate/', views.lettercreate, name='lettercreate'),
    path('letterupdate/<int:letter_id>', views.letterupdate, name='letterupdate'),
    path('letterdelete/<int:letter_id>', views.letterdelete, name='letterdelete'),
    path('commentcreate/<int:letter_id>', views.commentcreate, name='commentcreate'),
    path('getrandom/', views.getrandom, name='getrandom'),
    path('yoursort/<int:letter_id>', views.yoursort, name='yoursort'),
    path('home/', views.home, name='home'),
]