from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
import uuid

class PledgeClass(models.Model):
    season = models.CharField(max_length = 10, blank = True)
    year = models.CharField(max_length = 10, blank = True)
    name = models.CharField(max_length = 40, blank = True)
    class_number = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
            try:
                print (self.name)
                existing = PledgeClass.objects.get(name = self.name)
                self.id = existing.id
            except PledgeClass.DoesNotExist:
                pass
            models.Model.save(self, *args, **kwargs)

class Alumni(models.Model):
    user = models.OneToOneField(User)
    employer = models.CharField(blank = True, max_length = 100)
    position = models.CharField(blank = True, max_length = 100)
    current_city = models.CharField(blank = True, null = True, max_length = 50)
    phone = models.CharField(blank = True, max_length = 50)
    major = models.CharField(blank = True, max_length = 100)
    bio = models.CharField(blank = True, max_length = 500)
    position_description = models.CharField(blank = True, max_length = 500)
    picture = models.FileField(blank = True)
    company_logo = models.FileField(blank = True)
    family = models.CharField(blank = True, max_length = 100)
    nickname = models.CharField(blank = True, max_length = 100)
    graduation_class = models.CharField(blank = True, max_length = 100)
    hometown = models.CharField(blank = True, max_length = 100)
    confirmation_code = models.CharField(max_length = 36)
    pledge_class = models.ForeignKey(PledgeClass, null = True, blank = True)
    created_at = models.DateTimeField(blank = True, auto_now = True, null = True)
    updated_at = models.DateTimeField(blank = True, auto_now_add = True, null = True)
    number = models.IntegerField(null = True, blank = True)
    big = models.ForeignKey(self, null = True, blank = True)

    def __unicode__(self):
        return self.user.first_name + " " +  self.user.last_name

    def __str__(self):
        return self.user.first_name + " " +  self.user.last_name

    def save(self, *args, **kwargs):
            try:
                existing = Alumni.objects.get(user = self.user)
                self.id = existing.id
            except Alumni.DoesNotExist:
                pass
            models.Model.save(self, *args, **kwargs)



def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Alumni.objects.get_or_create(user = instance)

post_save.connect(create_profile, sender = User)
