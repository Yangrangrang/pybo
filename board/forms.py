'''
파일명 : forms.py
설 명 : html form 관리
생성일 : 2023/02/01
생성자 : yanghanna
'''

from django import forms
from board.models import Board

class BoardFrom(forms.ModelForm):
    class Meta:
        model = Board   # 사용할 question model

        fields = ['subject','content'] # QuestionForm 사용할 question model의 속성
        # widgets = { # 속성 추가
        #     # class = "form-control"
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control','rows':10}),
        # }
        labels = {  # subject -> 제목으로 변경
            'subject' : '제목',
            'content' : '내용',
        }