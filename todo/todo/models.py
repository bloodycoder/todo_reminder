from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=120)
    status = models.IntegerField(max_length=50)
    create_date  = models.DateTimeField('create date')
    def __unicode__(self):
        return self.name
