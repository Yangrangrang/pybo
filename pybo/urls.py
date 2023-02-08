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

    # answer
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    #answer_modify
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    #answer_delete
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

    # pybo:detail
    path('<int:question_id>/',views.detail,name='detail'),
    # pybo:question_create
    path('question/create/',views.question_create,name='question_create'),
    #pybo:question_modify
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    #pybo:question_delete
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),

    #temp menu
    path('boot/menu/', views.boot_menu, name='boot_menu'),

    # bootstrap template
    path('boot/list/', views.boot_list, name='boot_list'),
    path('boot/reg/', views.boot_reg, name='boot_reg'),

    #crawling
    path('crawling/cgv/', views.crawling_cgv, name='crawling_cgv'),
]