from django.db import models
from django.urls import reverse
# Create your models here.
class Tutorrecords(models.Model):

    topic = models.CharField(max_length=255, blank=True, null=True )
    subject = models.CharField(max_length=500,  blank=True, null=True)
    document = models.FileField( upload_to="Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True,)
    pages = models.IntegerField(default=0,  blank=True, null=True)
    style = models.CharField(max_length=255,  blank=True, null=True)
    amount = models.IntegerField(default=0.0, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('/')