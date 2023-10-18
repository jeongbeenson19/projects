from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question, Category


def index(request, category_name='qna'):
    """
    pybo 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    so = request.GET.get('so', 'recent') # 정렬 기준

    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    question_list = Question.objects.filter(category=category)


    # 정렬

    if so == 'recommend':
        question_list = question_list.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # recent
        question_list = question_list.order_by('-create_date')
    
    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여 주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so, 'category_list': category_list, 'category': category}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
