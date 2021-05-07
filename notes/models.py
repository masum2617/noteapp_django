from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Notes(models.Model):
    note_title = models.CharField(max_length=30)
    note_content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_title

    def get_absolute_url(self):
        return reverse('notes-content') # takes you to home page/or any page by given name after submitting the notes

    class Meta:
        verbose_name_plural = 'Notes'
