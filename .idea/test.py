import sys
import urllib.request
from bs4 import BeautifulSoup


def __init__(self):
    # Naver 환율 페이지 크롤링(Crawling) 작업
    fp = urllib.request.urlopen('http://info.finance.naver.com/marketindex/exchangeList.nhn')
    source = fp.read()
    fp.close()

    # 크롤링한 정보
    # tit - 통화명
    # sale - 매매기준율
    class_list = ["tit", "sale"]

    # BeautifulSoup으로 html소스를 python객체로 변환
    # (html소스코드, 이용할 parser)
    # python 내장 html.parser를 이용
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all("td", class_=class_list)

    # 각 국가별 환율 정보 저장
    money_data = {}
    for data in soup:
        if soup.index(data) % 2 == 0:
            data = data.get_text().replace('\n', '').replace('\t', '')  # HTML 태그 제거
            money_key = data  # key 값에 통화명 저장
        elif soup.index(data) % 2 == 1:
            money_value = data.get_text()
            money_data[money_key] = money_value  # 통화명 key 값에 각각의 매매기준율 저장
            money_key = None
            money_value = None

    # 사전 money_data를 리스트 money_data_keys, money_data_values로 변환
    money_data_keys = []
    money_data_values = []

    for key, values in money_data.items():
        money_data_keys.append([key])
        money_data_values.append([values])

    print(money_data_keys)