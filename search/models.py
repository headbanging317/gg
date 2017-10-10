from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField()

    def __unicode__(self):
        return self.url