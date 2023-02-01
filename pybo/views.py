from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question
from .forms import QuestionFrom

def question_create(request):
    '''질문 등록'''
    print('request.method:{}'.format(request.method))
    if request.method == 'POST':
        # print('question_create post')
        # 저장
        form = QuestionFrom(request.POST)   # request.POST 데이터 (subject,content 자동 생성)
        if form.is_valid(): # form(질문등록)이 유효하면
            question = form.save(commit=False) # subject, content만 저장 (확정(commit)은 하지 않음)
            question.create_date = timezone.now()
            question.save() # 확정
            return redirect("pybo:index")
    else:
        form = QuestionFrom()
    context = {'form': form}
    return render(request, 'pybo/question_form.html',context)

'''bootstrap list'''
def boot_menu(request):
    '''개발에 사용되는 임시 메뉴'''
    return render(request, 'pybo/menu.html')

def boot_reg(request):
    '''bootstrap reg'''
    return render(request, 'pybo/reg.html')

def boot_list(request):
    '''bootstrap template'''
    return render(request, 'pybo/list.html')

def answer_create(request,question_id):
    print('answer_create:{}'.format(question_id))
    question = get_object_or_404(Question, pk=question_id)
    # Question과 Answer 처럼 서로 연결되어 있는 경우
    # 연결 모델명 _set 연결데이터를 조회할 수 있다.

    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail',question_id=question.id)

def detail(request,question_id):
    '''question 상세'''
    print('1.question_id:{}'.format(question_id))
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    print('2.question:{}'.format(question))
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

# Create your views here.
def index(request):
    # return HttpResponse('Hello pybo에요')
    '''question 목록'''
    # list order create_date desc
    print('index 레벨로 출력')
    question_list = Question.objects.order_by('create_date')    # order_by('-필드') desc, asc order_by('필드')
    # question_list =Question.objects.filter(id=99)
    context = {'question_list':question_list}
    print('question_list:{}'.format(question_list))
    return render(request, 'pybo/question_list.html', context)

