from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField()

    def __unicode__(self):
        return self.url



class Full2(models.Model):
    content2 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name2    