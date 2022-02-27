from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


def get_sector(url):
    ########### URL 가져오기 #############

    try:  # try: url을 열 수 있는 경우
        base_url = urlopen(url)
    except HTTPError as e:  # except: url 열 수 없는 경우(사번에 해당하는 정보 페이지 없음  - HTTPError)
        return ['None'] * len(targets)  # url 열지 못하는 경우 None 출력

    bs = BeautifulSoup(base_url, 'html.parser')
    bs = bs.find('table', {'class': 'table_guide01'})
    th = bs.find_all('th')
    td = bs.find_all('td')

    target_list = [t.text for t in th]

    data = []
    for t in targets:
        try:
            idx = target_list.index(t)
            data.append(td[idx].text)
        except:
            data.append('None')

    return data


def get_title(url):
    try:
        base_url = urlopen(url)
    except HTTPError as e:
        return 'None'

    try:
        bs = BeautifulSoup(base_url, 'html.parser')
        title = bs.find('div', class_='titles').find('h4').text  # div 태그에서 titles -  h4 가 회사명을 포함하고 있음
    except:
        return 'None'  # url 열지 못하는 경우 회사명 대신 None 출력

    return title


url = 'https://bizno.net/article/1388189857'

# get crawling data
sector = get_sector(url)
title = get_title(url)