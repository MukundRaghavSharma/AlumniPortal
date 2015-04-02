from django.contrib import admin
from Alumni.models import Alumni, PledgeClass
from image_cropping import ImageCroppingMixin

admin.site.register(Alumni)
admin.site.register(PledgeClass)
