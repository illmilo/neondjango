from django.db import models

# Create your models here.
class Tutorial(models.Model):
    video = models.FileField(upload_to='videos/', null=True, blank=True)
