import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목'   ) # 길이 제한이 있다.
    content = models.TextField(help_text='Markdown 문법을 써주세요.', verbose_name='내용')             # 길이 제한이 없다.
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
        blank=True,
        validators=[lnglat_validator],
        help_text='경도,위도 포맷으로 입력',)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)