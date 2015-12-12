from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    budget = models.CharField(max_length=50)
    like = models.CharField(max_length=300)
    dislike = models.CharField(max_length=300)  
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=50)

    def __unicode__(self):
        return self.name