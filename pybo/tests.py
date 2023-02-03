from django.test import TestCase

# Create your tests here.
import unittest
import datetime
import logging
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# ---------------------------------------------
from pybo.models import Question
from django.utils import timezone

'''
for i in range(500):
    q = Question(subject='금요일 입니다.[%3d]'% i, content='즐거운 금요일!', create_date=timezone.now())
    q.save()

'''
# ---------------------------------------------


class Crawling(unittest.TestCase):

    def test_naver(self):
        self.brower.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

        id_textinput = self.brower.find_element(By.ID, 'id')
        id_textinput.send_keys('good_day')

        pw_textinput = self.brower.find_element(By.ID, 'pw')
        pw_textinput.send_keys('4321')

        btn_login = self.brower.find_element(By.ID, 'log.login')
        btn_login.click()   # 버튼 클릭
        pass


    def setUp(self):
        self.brower = webdriver.Firefox(executable_path='/Users/yanghanna/Downloads/geckodriver')
        print('setup')

    def tearDown(self):
        print('tearDown')
        # self.brower.quit()    # webdriver 종료

    def test_selenium(self):
        # 파이어폭스 웹 드라이버 객체에게 Get을 통하여 네이버의 http요청을 하게 함.
        self.brower.get('http://127.0.0.1:8000/pybo/9/')
        print('self.brower.title:{}'.format(self.brower.title))
        self.assertIn('Pybo', self.brower.title)

        content_textarea = self.brower.find_element(By.ID, 'content')
        content_textarea.send_keys('오늘은 아주 즐거운 금요일!')

        btn = self.brower.find_element(By.ID, 'submit_btn')
        btn.click()     # 버튼 클릭
        pass

    def jusik(self,code):
        url = 'https://finance.naver.com/item/main.naver?code='
        # sam = '005930'
        # hun = '005380'
        return url + code

    def test_juju(self):
        response = requests.get(self.jusik('005930'))
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html,'html.parser')

            # 주가
            price = soup.select('p.no_today em.no_up span.blind')
            print(price[0].getText())


    def test_naver_stock(self):
        '''주식 크롤릴'''
        codes = {'삼성정자':'005930', '현재차':'005380'}
        for code in codes.keys():
            url = 'https://finance.naver.com/item/main.naver?code='
            url = url + str(codes[code])

            response = requests.get(url)
            if 200 == response.status_code:
                html = response.text
                soup = BeautifulSoup(html,'html.parser')

                price = soup.select_one('#chart_area div.rate_info div.today span.blind')
                print('today:{},{},{}'.format(code,codes[code],price.getText()))
            else:
                print("페이지 오류 response.status_code:{}".format(response.status_code))
        pass

    def test_slem(self):
        url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=223800&target=after&page='
        for i in range(1,4,1):
            self.call_slemdunk(url+str(i))

    def call_slemdunk(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html,'html.parser')

            # 평점
            score = soup.select('div.list_netizen_score em')
            #감상폄
            review = soup.select('table tbody tr td.title')

            for i in range(0, len(score)):
                review_text = review[i].getText().split('\n')

                if len(review_text>2):  # 평점만 넣고 감상평이 없는 경우 처리
                    tmp_text = review_text[5]
                else:
                    tmp_text = review_text[0]
            print('평점,감상평:{},{}'.format(score[i].getText(), tmp_text))

        else:
            print("페이지 오류 response.status_code:{}".format(response.status_code))


    def test_slemdumk(self):    # 내가 한거 미완성
        ''' https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=223800&target=after&page=1 '''
        url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=223800&target=after&page='
        for i in range(1,4,1):
            # print('page:{}'.format(type(i)))
            # st = str(i)
            response = requests.get(url)
            # print(response.status_code)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html,'html.parser')
                # print(soup)
                review = soup.select('td.title')
                str = review[2].getText().split('\n')
                str1 = ""
                # print(str[5])

                for rows in range(0,10,1):
                    reviewtotal = review[rows].getText().split('\n')
                    if len(reviewtotal) > 2:
                        str1 = reviewtotal[5]
                        print(str1)
            else:
                print("페이지 오류 response.status_code:{}".format(response.status_code))

    def test_cgv(self):
        '''CGV http://www.cgv.co.kr/movies/?lt=1&ft=0 '''
        url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
        response = requests.get(url)
        print('response.status_code:{}'.format(response.status_code))   # 200이면 성공
        if response.status_code == 200:
            html = response.text
            # print('html:{}'.format(html))
            # box-contents
            soup = BeautifulSoup(html,'html.parser')
            # 제목
            title = soup.select('div.box-contents strong.title')
            # print('title:{}'.format(title))

            # 예매율
            reserve = soup.select('div.score strong.percent span')

            # 포스터
            poster = soup.select('span.thumb-image img')

            # 다건이기 때문에 뺑뻉이(for문)
            for page in range(0,7,1):
                posterImg = poster[page]
                imgUrlPath = posterImg.get('src')   # <img src=''> 에 접근
                print('title[page]:{},{},{}'.format(title[page].getText(), reserve[page].getText(),imgUrlPath))
                # print('imgUrlPath:{}'.format(imgUrlPath))
        else:
            print('접속 오류 response.status_code:{}'.format(response.status_code))

    @unittest.skip('테스트연습')
    def test_weather(self):
        '''날씨'''
        # https://weather.naver.com/today/09545101
        now = datetime.datetime.now()
        # yyyymmdd hh:mm
        newDate = now.strftime('%Y-%m-%d %H:%M:%S')
        print('now:{}'.format(now))
        print('newDate:{}'.format(newDate))

        naverWetherUrl = 'https://weather.naver.com/today/09545101'
        html = urlopen(naverWetherUrl)
        # print('html:{}'.format(html))
        bsObject = BeautifulSoup(html,'html.parser')
        tmpes = bsObject.find('strong','current')
        print('금천구 가산동:{}'.format(tmpes.getText()))

        print('test_weather')
        pass

    ''' 여러개의 list를 묶어서 하나의 iterable 객체로 다룰 수 있게 한다.'''
    def test_zip(self):
        pass