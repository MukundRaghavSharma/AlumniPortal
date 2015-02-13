from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(null = True, max_length = 100)
    last_name = models.CharField(null = True, max_length = 100)
    employer = models.CharField(null = True, max_length = 100)
    current_city = models.CharField(null = True, max_length = 50)
    phone = models.CharField(null = True, max_length = 50)
    major = models.CharField(null = True, max_length = 100)
    email = models.EmailField()
    graduation_class = models.CharField(null = True, max_length = 100)
    hometown = models.CharField(null = True, max_length = 100)
    pledge_class = models.CharField(null = True, max_length = 15)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.first_name + " " +  self.last_name
