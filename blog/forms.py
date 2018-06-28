#ModelForm 을 상속받는 PostModelFrom 클래스
from django import forms
from .models import Post
from .models import min_length_3_validateor

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validateor])
    text = forms.CharField(widget=forms.Textarea)