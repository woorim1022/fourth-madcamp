from django import forms # 장고에서 제공하는 forms 기능을 사용하기 위해
from .models import Letter, Comment# Post 모델을 사용하기 위해 import

class LetterForm(forms.ModelForm): # PostForm이라는 이름의 모델폼 클래스 생성
    class Meta:
        model = Letter # form에서 사용할 모델이 Post임을 명시
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']