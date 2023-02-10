'''
파일명 : answer_views.py
설 명 : 
생성일 : 2023/02/08
생성자 : yanghanna
'''

import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import AnswerFrom
from ..models import Question, Answer
#ctrl + alt + o(alpa): import정리

@login_required(login_url='common:login')
def answer_vote(request, answer_id):
    logging.info('1. answer_vote:{}'.format(answer_id))
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user == answer.author:
        messages.error(request, '본인이 작성한 댓글은 추천 할 수 없습니다.')
    else:
        answer.voter.add(request.user)

    return redirect('pybo:detail', question_id=answer.question.id)


@login_required(login_url='common:login')   # 로그인이 되어있지 않으면 login 페이지로 이동
def answer_create(request, question_id):
    '''답변등록'''

    logging.info('1.answer_create:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerFrom(request.POST)
        if form.is_valid():
            logging.info('2.answer_create:{}'.format(question_id))
            answer = form.save(commit=False)    # content만 저장 (commit은 하지 않음)
            answer.create_date = timezone.now()
            answer.question = question
            answer.author = request.user  # author 속성에 로그인 계장 저장

            logging.info('answer.author:{}'.format(answer.author))

            answer.save()   # 최종 저장
            return redirect('pybo:detail', question_id=question.id)
    else :
        form = AnswerFrom()

    # form validation
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

    # Question과 Answer 처럼 서로 연결되어 있는 경우
    # 연결 모델명 _set 연결데이터를 조회할 수 있다.
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail',question_id=question.id)



def answer_modify(request, answer_id):
    logging.info('1. answer_modify():{}'.format(answer_id))
    #1. answer id에 해당되는 데이터 조회
    #2. 수정 권한 체크: 권한이 없는 경우 메시지 전달
    #3. POST : 수정
    #4. GET : 수정 Form 전달

    #1.
    answer = get_object_or_404(Answer, pk=answer_id)

    #2.
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        # 수정 화면
        return redirect('pybo:detail', question_id=answer.question.id)

    #3.
    if request.method == "POST":    # 수정
        form = AnswerFrom(request.POST, instance=answer)
        logging.info('2. answer_modify POST answer:{}'.format(answer))
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            # 수정 화면
            return redirect('pybo:detail', question_id=answer.question.id)
    else:                           # 수정 template
        form = AnswerFrom(instance=answer)

    context = {'answer':answer, 'form':form}
    return render(request, 'pybo/answer_form.html', context)



@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    logging.info('1. answer_delete():{}'.format(answer_id))
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question.id)
    else:
        answer.delete()

    return redirect('pybo:detail', question_id=answer.question_id)

