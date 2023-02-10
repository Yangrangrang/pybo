from django.db import models
from django.contrib.auth.models import User

# 질문 Question 클래스 생성 : subject, content, create_date
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 200크기만큼의 varchar 글자수 제한
    content = models.TextField()  # 글자수 제한이 없는 경우
    create_date = models.DateTimeField() # 날짜 + 시간

    #author 필드 추가 : 글쓴이
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_question')
    # 회원테이블에 사용자 정보가 삭제 되면 Question 테이블에 질문도 동일하게 모두 삭제

    # 수정일시 추가
    modify_date = models.DateTimeField(null=True, blank=True)
    # 데이터 베이스에서 null 허용 (null=True)
    # form.is_valid() 입력값 검증 시 값이 없어도 된다. (blank=True)

    # 추천인
    voter = models.ManyToManyField(User, related_name='voter_question')


    def __str__(self):
        return self.subject

class Answer(models.Model):
    # 답변의 연관된 질문이 삭제되면 답변도 모두 삭제 하세요. (on_delete=models.CASCADE())
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()    # 글자수 제한이 없는
    create_date = models.DateTimeField()    # 날짜 + 시간

    # author 필드 추가: 글쓴이
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    # 입력 필드에 null gjdydgkrl
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # 수정일시 추가
    modify_date = models.DateTimeField(null=True, blank=True)
    # 추천인
    voter = models.ManyToManyField(User, related_name='voter_answer')