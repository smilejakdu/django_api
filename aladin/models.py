from django.db import models


# Create your models here.

class Aladin(models.Model):
    title = models.CharField(max_length=250, verbose_name='title')
    price = models.CharField(max_length=200, verbose_name='price')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'aladins'
