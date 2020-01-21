from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin


# Create your models here.
class Letter(models.Model):
    writer = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='letters')
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=200)
    letter_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    @property
    def update_counter(self):
        self.letter_hit = self.letter_hit + 1
        self.save()

class Comment(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

class Emogi(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    letter = models.ForeignKey(Letter, null=True, on_delete=models.CASCADE)
    smile = models.PositiveIntegerField(default=0)
    panic = models.PositiveIntegerField(default=0)
    happy = models.PositiveIntegerField(default=0)
    sad = models.PositiveIntegerField(default=0)
    funny = models.PositiveIntegerField(default=0)
    angry = models.PositiveIntegerField(default=0)
    embarass = models.PositiveIntegerField(default=0)
    love = models.PositiveIntegerField(default=0)


class Mywrite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    writecount = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True)



class Myhit(models.Model):
    hitter = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hit = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True)

   