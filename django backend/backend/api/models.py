from django.db import models

# Create your models here.
class Quote(models.Model) :
    quote = models.CharField(max_length=500, blank=False, null=False)