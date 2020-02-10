from django.db import models


# Create your models here.

# TextField 굳이 max_length 를 해도 된다. 길이를 이정도 생각하고 있구나 라는 생각을 하면된다. 제한을 두고싶으면 코드로 제한을 둬야한다.
# MnayToManyFiled 란 무엇인가 ? = => 테이블에 필드 잡히지 않는다. == > 로직화 연결 관계

class Comment(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    comment = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'  # table 명은 복수로 해야함
