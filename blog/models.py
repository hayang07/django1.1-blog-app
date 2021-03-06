from django.db import models
from django import forms
from django.utils import timezone

def min_length_3_validateor(value):
    if len(value) < 3:
        #강제 에러
        raise forms.ValidationError('3글자 이상 입력해 주세요.')

# Create your models here.
class Post(models.Model):
    #작성자
    author = models.ForeignKey('auth.User')
    #제목
    title = models.CharField(max_length=200,validators=[min_length_3_validateor])
    #내용  not null
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

