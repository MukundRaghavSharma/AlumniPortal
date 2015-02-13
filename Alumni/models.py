from django.db import models

class Alumni(models.Model):
    first_name = models.CharField(null = True, max_length = 100)
    last_name = models.CharField(null = True, max_length = 100)
    employer = models.CharField(null = True, max_length = 100)
    current_city = models.CharField(null = True, max_length = 50)
    email = models.EmailField(null = True)
    graduation_class = models.IntegerField(null = True)
    hometown = models.CharField(null = True, max_length = 100)
    pledge_class = models.CharField(null = True, max_length = 15)
    time_stamp = models.DateTimeField(auto_now_add = True)
