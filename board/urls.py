from django.urls import path
from .views import base_views,board_views

app_name = 'board'

urlpatterns = [
    #view
    path('', base_views.index, name='index'),
    path('<int:board_id>/',base_views.detail,name='detail'),

    path('board/create/', board_views.board_create, name='board_create'),
    # path('board/modify/<int:board_id>/', board_views.question_modify, name='board_modify'),
    # path('board/delete/<int:board_id>/', board_views.question_delete, name='board_delete'),

]
