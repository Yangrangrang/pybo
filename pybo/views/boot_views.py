'''
파일명 : boot_views.py
설 명 : 
생성일 : 2023/02/08
생성자 : yanghanna
'''

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
#ctrl + alt + o(alpa): import정리


def crawling_cgv(request):
    ''' CGV 무비차트'''
    url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
    response = requests.get(url)

    context = {}
    if response.status_code == 200:
        html = response.text
        # print('html:{}'.format(html))
        # box-contents
        soup = BeautifulSoup(html, 'html.parser')
        # 제목
        title = soup.select('div.box-contents strong.title')
        # print('title:{}'.format(title))

        # 예매율
        reserve = soup.select('div.score strong.percent span')

        # 포스터
        poster = soup.select('span.thumb-image img')

        title_list=[]   # 제목
        reserve_list = []   # 에매율
        poster_list = []     # 포스터

        # 다건이기 때문에 뺑뻉이(for문)
        for page in range(0, 7, 1):
            posterImg = poster[page]
            imgUrlPath = posterImg.get('src')  # <img src=''> 에 접근
            title_list.append(title[page].getText())
            reserve_list.append(reserve[page].getText())
            poster_list.append(imgUrlPath)
            print('title[page]:{},{},{}'.format(title[page].getText(), reserve[page].getText(), imgUrlPath))
            # print('imgUrlPath:{}'.format(imgUrlPath))

        # 화면에 title을 []전달
        context = {'context': zip(title_list,reserve_list,poster_list)}
    else:
        print('접속 오류 response.status_code:{}'.format(response.status_code))
    pass

    return render(request, 'pybo/crawling_cgv.html',context)


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
