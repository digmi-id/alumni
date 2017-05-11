from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Alumni(models.Model):
    nis = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    place_birth = models.CharField(max_length=50)
    date_birth = models.DateField('tanggal lahir')
    address = models.CharField(max_length=255)


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=255)


@python_2_unicode_compatible
class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    place_birth = models.CharField(max_length=50)
    date_birth = models.DateField('tanggal lahir')
    address = models.CharField(max_length=255)
