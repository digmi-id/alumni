from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Alumni(models.Model):
    KULIAH = "KULIAHL"
    KERJA = "KERJA"
    STATUS = (
        (KULIAH, "KULIAH"),
        (KERJA, "KERJA"),
    )
    nis = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    place_birth = models.CharField(max_length=50)
    date_birth = models.DateField('tanggal lahir')
    address = models.CharField(max_length=255)
    photo = models.FileField(upload_to='alumni/photo/')
    generation = models.CharField(max_length=4)
    status = models.CharField(max_length=6, choices=STATUS, default='KL')
    def is_superclass(self):
        return self.status in (self.KULIAH, self.KERJA)

@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=255)