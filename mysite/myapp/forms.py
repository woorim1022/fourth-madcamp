from django import forms # 장고에서 제공하는 forms 기능을 사용하기 위해
from .models import Letter, Comment# Post 모델을 사용하기 위해 import
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin

class LetterForm(forms.ModelForm): # PostForm이라는 이름의 모델폼 클래스 생성
    class Meta:
        model = Letter # form에서 사용할 모델이 Post임을 명시
        fields = ['title','body']

        widgets = {
            'body': forms.Textarea(
                attrs={
                    'style': 'background-color:#00ff0000',
                    'cols': '32.5',
                    'rows' : '7',
                }
            )
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']