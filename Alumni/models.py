from django.db import models

class Alumni(models.Model):
    name = models.CharField(max_length = 100)
    employer = models.CharField(max_length = 100)
    current_city = models.CharField(max_length = 50)
    email = models.EmailField()
    graduation_year = models.IntegerField()
    hometown = models.CharField(max_length = 100)
    pledge_class = models.CharField(max_length = 15)
