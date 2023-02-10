'''
파일명 : question_views.py
설 명 : 
생성일 : 2023/02/08
생성자 : yanghanna
'''

import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionFrom
from ..models import Question
#ctrl + alt + o(alpa): import정리
@login_required(login_url='common:login')
def question_vote(request,question_id):
    '''질문: 좋아요'''
    logging.info('1. question_vote question_id:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)

    #본인글은 추천 하지 못하게
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천 할 수 없습니다.')
    else:
        question.voter.add(request.user)

    return redirect('pybo:detail', question_id=question.id)
    pass


@login_required(login_url='common:login')
def question_create(request):
    '''질문 등록'''
    logging.info('request.method:{}'.format(request.method))
    if request.method == 'POST':
        # logging.info('question_create post')
        # 저장
        form = QuestionFrom(request.POST)   # request.POST 데이터 (subject,content 자동 생성)
        if form.is_valid(): # form(질문등록)이 유효하면
            question = form.save(commit=False) # subject, content만 저장 (확정(commit)은 하지 않음)
            question.create_date = timezone.now()
            question.author = request.user #author 속성에 로그인 계정 저장

            logging.info('question.author:{}'.format(question.author))

            question.save() # 확정
            return redirect("pybo:index")
    else:
        form = QuestionFrom()
    context = {'form': form}
    return render(request, 'pybo/question_form.html',context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    '''질문 수정 : login 필수'''
    logging.info('1. question_modify')
    question = get_object_or_404(Question, pk=question_id)  # question id로 Question 조회

    # 권한 체크
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == 'POST':
        logging.info('2. question_modify post')
        form = QuestionFrom(request.POST, instance=question)

        if form.is_valid():
            logging.info('3. form.is_valid():{}'.format(form.is_valid()))
            question = form.save(commit=False)  # 질문내용,
            question.modify_date = timezone.now()   # 수정 일시 저장
            question.save()
            return redirect("pybo:detail", question_id=question.id)
    else:
        form = QuestionFrom(instance=question)  # get 수정할 데이터 전달
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    logging.info('1. question_delete')
    logging.info('2. question_id:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error('삭제 권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    question.delete()   #삭제
    return redirect('pybo:index')