from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# from django_autoslug.fields import AutoSlugField # intallled pip install django-autoslug-field ?

# Create your models here.
# In models.py each class is a table in the database and each variable is a column

class DojoMemberType(models.Model):
    member_type = models.CharField(max_length=20, verbose_name='Type of Member', help_text='Student or Instructor')

    def __unicode__(self):
        return self.member_type

class DojoMember(models.Model):
    f_name = models.CharField(max_length=50, verbose_name='First Name')
    l_name = models.CharField(max_length=50, verbose_name='Last Name')
    position = models.ManyToManyField(DojoMemberType)
    email = models.EmailField(blank=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.f_name



