'''
파일명 : urls.py
설 명 : 로그인/ 로그아웃
생성일 : 2023/02/06
생성자 : yanghanna
'''


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    # django.contrib.auth앱의 LoginView 클래스를 활용
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login')
]