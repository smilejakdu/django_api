from django.db import models


# Create your models here.

class BestSearch(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'best_search_views'
