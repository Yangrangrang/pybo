"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from pybo.models import Question, Answer
from django.utils import timezone

# q = Question(subject='파이썬 게시판은 무엇인가요', content = '알고싶어요!', create_date=timezone.now())
# q = Question(subject='장고 모델은 무엇인가요', content = 'id는 자동으로 생성되나요!', create_date=timezone.now())
# q.save()

# 전체 데이터 조회
# Question.objects.all()

# Question.objects.filter(id=2) # return형 QuerySet을 내부적으로 돌려준다.
# 데이터가 1건인 경우 get (데이터가 없는 경우 예외 발생)
# q = Question.objects.get(id=2)

# q.subject = 'Django Model Question'
# q = Question.objects.get(id=2)
# q.delete()

# a = Answer(question=q , content='id는 자동 생성됩니다.', create_date=timezone.now())
# a.save()

# 데이터 조회
# a = Answer.objects.get(id=1)

# question 데이터 조회
# a.question

# question에서 연관된 answer 모두 찾기
# q.answer_set.all()




urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls'))
]
