from django import forms
from .models import Post

#일반 폼이 아닌 모델폼 사용
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')