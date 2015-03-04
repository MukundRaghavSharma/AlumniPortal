from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class PledgeClass(models.Model):
    season = models.CharField(max_length = 10, blank = True)
    year = models.CharField(max_length = 10, blank = True)
    name = models.CharField(max_length = 40, blank = True)

    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
            try:
                existing = PledgeClass.objects.get(name = self.name)
                self.id = existing.id
            except PledgeClass.DoesNotExist:
                pass
            models.Model.save(self, *args, **kwargs)

class Alumni(models.Model):
    user = models.OneToOneField(User)
    employer = models.CharField(blank = True, max_length = 100)
    position = models.CharField(blank = True, max_length = 100)
    current_city = models.CharField(blank = True, max_length = 50)
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
    pledge_class = models.ForeignKey(PledgeClass, null = True, blank = True)
    created_at = models.DateTimeField(blank = True, auto_now = True, null = True)
    updated_at = models.DateTimeField(blank = True, auto_now_add = True, null = True)
    number = models.IntegerField(null = True, blank = True)
    #big = models.OneToOneField(User)
    #littles = models.ForeignKey(User)

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

def social_auth_to_profile(backend, details, response, user=None, is_new=False, *args, **kwargs):
    # Stuff to parse from LinkedIn:
    # 1. Employer
    # 2. Summary 
    # 3. Position
    # 4. LinkedIn Public Page URL
    # 5. Picture URL

    # Check for each field.. some could be None #
    first_name = details['first_name']
    last_name = details['last_name']
    email = details['email']
    '''
    if first_name not in details:
        first_name = ''
    if last_name not in details:
        last_name = ''
    if email not in details:
        email = ''
    alumni = None
    '''
    if is_new:
        # Create new profile here #
        user = User.objects.get_or_create(first_name = first_name, last_name = last_name, email = email)
    else:
        # Not new -> link to already created profile #
        user = User.objects.get(first_name = first_name, last_name = last_name, email = email)
        alumni = Alumni.objects.get(user = user)

    alumni = Alumni.objects.get(user = user) 
    linkedin_info = kwargs['social'].extra_data
    alumni.role = str(linkedin_info['headline'])
    #alumni.position_description = linkedin_info['summary'] 
    #alumni.= social_user.extra_data['positions']['position'][0]['title']
    user.save()
    alumni.save()

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Alumni.objects.get_or_create(user = instance)

post_save.connect(create_profile, sender = User)
