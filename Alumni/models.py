from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Alumni(models.Model):
    user = models.OneToOneField(User)
    employer = models.CharField(blank = True, max_length = 100)
    position = models.CharField(blank = True, max_length = 100)
    current_city = models.CharField(blank = True, max_length = 50)
    phone = models.CharField(blank = True, max_length = 50)
    major = models.CharField(blank = True, max_length = 100)
    bio = models.CharField(blank = True, max_length = 500)
    picture = models.FileField(blank = True)
    company_logo = models.FileField(blank = True)
    family = models.CharField(blank = True, max_length = 100)
    nickname = models.CharField(blank = True, max_length = 100)
    graduation_class = models.CharField(blank = True, max_length = 100)
    hometown = models.CharField(blank = True, max_length = 100)
    pledge_class = models.ForeignKey(PledgeClass)
    created_at = models.DateTimeField(blank = True, auto_now = True, null = True)
    updated_at = models.DateTimeField(blank = True, auto_now_add = True, null = True)

    def __unicode__(self):
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

'''
class PledgeClass:
    alumni = models.OneToManyField(Alumni)
    season = models.CharField(max_length = 10)
    name = models.CharField(max_length = 40)

    def __unicode__(self):
        return self.name
'''
    '''
    def save(self, *args, **kwargs):
            try:
                existing = PledgeClass.objects.get(pledr = self.user)
                self.id = existing.id
            except PledgeClass.DoesNotExist:
                pass
            models.Model.save(self, *args, **kwargs)
    '''
'''
class AlumniRelationship(models.Model):
        big = models.ManyToOneField("Big", related_name='', verbose_name="Siblings", null=True, blank=True)
    big = models.OneToOneField(Alumni)
    little = models.OneToManyField(Alumni)
'''
