from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model


class Room(Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null =True, blank = True)
    participants = models.ManyToManyField(User, related_name= "participants", blank = True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ["-created", "name", "-updated" ]

    def __str__(self):
        return self.name

class Message(Model):
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created","-updated"]

    def __str__(self):
        return self.body[0:50]

