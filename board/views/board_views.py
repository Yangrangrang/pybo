import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import BoardFrom
from ..models import Board

# Create your views here.
@login_required(login_url='common:login')
def board_create(request):
    '''질문 등록'''
    logging.info('request.method:{}'.format(request.method))
    if request.method == 'POST':
        # logging.info('question_create post')
        # 저장
        form = BoardFrom(request.POST)   # request.POST 데이터 (subject,content 자동 생성)
        if form.is_valid(): # form(질문등록)이 유효하면
            board = form.save(commit=False) # subject, content만 저장 (확정(commit)은 하지 않음)
            board.create_date = timezone.now()
            board.author = request.user #author 속성에 로그인 계정 저장

            logging.info('board.author:{}'.format(board.author))

            board.save() # 확정
            return redirect("pybo:index")
    else:
        form = BoardFrom()
    context = {'form': form}
    return render(request, 'pybo/question_form.html',context)