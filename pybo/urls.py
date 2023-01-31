'''
파일명 : urls.py
설 명 : pybo 모든 url과 view함수의 멥핑을 담당
생성일 : 2023/01/25
생성자 : yanghanna
'''

from django.urls import path

from . import views
# 현재 디렉토리에 views 모듈을 import!

app_name='pybo'

urlpatterns = [
    path('', views.index,name='index'),   #views의 index함수로 메핑
    path('<int:question_id>/',views.detail,name='detail'),
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    #temp menu
    path('boot/menu/', views.boot_menu, name='boot_menu'),

    # bootstrap template
    path('boot/list/', views.boot_list, name='boot_list'),
    path('boot/reg/', views.boot_reg, name='boot_reg'),
]