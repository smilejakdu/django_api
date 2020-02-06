from django.db import models


# Create your models here.


class Comment(models.Model):
    email = models.EmailField(max_length=200, verbose_name='이메일')
    comment = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comment'
