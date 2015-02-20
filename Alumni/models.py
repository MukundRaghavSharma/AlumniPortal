from django.db import models
from django.contrib.auth.models import User

# Inbuilt Django User fields - 1. first_name
#                              2. last_name
#                              3. username
#                              4. password 

class Alumni(models.Model):
    user = models.OneToOneField(User)
    employer = models.CharField(blank = True, max_length = 100)
    position = models.CharField(blank = True, max_length = 100)
    current_city = models.CharField(blank = True, max_length = 50)
    phone = models.CharField(blank = True, max_length = 50)
    major = models.CharField(blank = True, max_length = 100)
    bio = models.CharField(blank = True, max_length = 500)
    picture = models.FileField()
    company_logo = models.FileField()
    family = models.CharField(blank = True, max_length = 100)
    email = models.EmailField()
    nickname = models.CharField(blank = True, max_length = 100)
    graduation_class = models.CharField(blank = True, max_length = 100)
    hometown = models.CharField(blank = True, max_length = 100)
    pledge_class = models.CharField(blank = True, max_length = 15)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.first_name + " " +  self.last_name
'''
class AlumniRelationship(models.Model):
    big = models.OneToOneField(Alumni)
    little = models.OneToManyField(Alumni)
'''
