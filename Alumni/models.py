from django.db import models
from django.contrib.auth.models import User

class Alumni(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(null = True, max_length = 100)
    last_name = models.CharField(null = True, max_length = 100)
    employer = models.CharField(null = True, max_length = 100)
    position = models.CharField(null = True, max_length = 100)
    current_city = models.CharField(null = True, max_length = 50)
    phone = models.CharField(null = True, max_length = 50)
    major = models.CharField(null = True, max_length = 100)
    bio = models.CharField(null = True, max_length = 500)
    picture = models.FileField()
    family = models.CharField(null = True, max_length = 100)
    email = models.EmailField()
    graduation_class = models.CharField(null = True, max_length = 100)
    hometown = models.CharField(null = True, max_length = 100)
    pledge_class = models.CharField(null = True, max_length = 15)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.first_name + " " +  self.last_name

class AlumniRelationship(models.Model):
    big = models.OneToOneField(Alumni)
    little = models.OneToManyField(Alumni)
