from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Topic(models.Model):
    subject =models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board= models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular blog author """
        return reverse('topics-by-board', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.subject
  

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)
    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=50
        if len(self.message)>len_title:
            titlestring=self.message[:len_title] + '...'
        else:
            titlestring=self.message
        return titlestring
