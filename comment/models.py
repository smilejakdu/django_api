from django.db import models


# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    comment = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
