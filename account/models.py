from django.db import models


# Create your models here.


class Account(models.Model):
    email = models.EmailField(max_length=200, unique=True, verbose_name='email')
    name = models.CharField(max_length=200, unique=True, verbose_name='name')
    password = models.CharField(max_length=200, verbose_name='비밀번호')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'account'
