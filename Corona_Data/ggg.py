from bs4 import BeautifulSoup
import requests
import re
import datetime
from dateutil.relativedelta import relativedelta
from tqdm import tqdm
import sys
from newspaper import Article, Config  # 뉴스 홈페이지가 달라도 제목과 본문을 추출할수 있도록 도와주는 라이브러리임
from urllib.parse import quote_plus
from selenium import webdriver  # 사용하는 라이브러리가 다름
# 웹브라우저를 현실화한 라이브러리 직접클릭하고 스크롤하는 기능도 포함이됨
# 웹페이지의 html코드를 받아옴
import time
lang = {'korean': 'lang_ko', 'english': 'lang_en', 'spanish': 'lang_es', 'french': 'lang_fr', 'italiano': 'lang_it'}

search = sys.argv[1] if len(
    sys.argv) > 1 else '((코로나19) OR (코로나) OR (코로나 바이러스) OR (신종 코로나바이러스) OR (COVID-19) OR (코비드19) OR (우한폐렴))'
page = int(sys.argv[2]) if len(sys.argv) > 2 else 1
page2 = int(sys.argv[3]) if len(sys.argv) > 3 else 10
date = sys.argv[4] if len(sys.argv) > 4 else '2021-10-10'
l = sys.argv[5] if len(sys.argv) > 5 else 'korean'


def makePgNum(num):
    if num == 1:
        return num - 1
    elif num == 0:
        return num
    else:
        return 10 * (num - 1)


def makeUrl(search, date, language, start_pg, end_pg):
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://www.google.com/search?q=%s&tbs=cdr:1,cd_min:%s,cd_max:%s&tbm=nws&start=%s&lr=%s" \
              % (quote_plus(search), date.strftime("%m/%d/%Y"), (date + relativedelta(days=1)).strftime("%m/%d/%Y"),
                 start_page, language)
        return url

    # lr -> 언어, cd_min, cd_max - > 날짜 시작 끝일 지정

    else:
        urls = []
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://www.google.com/search?q=%s&tbs=cdr:1,cd_min:%s,cd_max:%s&tbm=nws&start=%s&lr=%s" \
                  % (quote_plus(search), date.strftime("%m/%d/%Y"), (date + relativedelta(days=1)).strftime("%m/%d/%Y"),
                     page, language)
            urls.append(url)
        return urls


def news_attrs_crawler(articles, attrs):
    attrs_content = []
    for i in articles:
        attrs_content.append(i.attrs[attrs])
    return attrs_content


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}


# 사람이 접속했다는 표시를 내기위함
# user agent string을 검색 -> 무엇이 나왔는지 확인하고 복사해서 사용하면 됨.

def articles_crawler(url):
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        # 크롬 드라이버를 설치해야함
        # 버전에 맞는 드라이버를 다운.
        driver.get(url)
        driver.implicitly_wait(10)
        # 데이터가 로드될때 까지 기다림.
        html = driver.page_source
        html = BeautifulSoup(html, "html.parser")  #
        url_google = html.select("#rso > div > div > div > div > div > a")
        url = news_attrs_crawler(url_google, 'href')
        driver.quit()
    except:
        url = []
    return url


date = datetime.datetime.strptime(date, "%Y-%m-%d")

url = makeUrl(search, date, lang[l], page, page2)

news_titles = []
news_url = []
news_contents = []
news_dates = []
idx = 1
for i in url:
    time.sleep(idx % 10)
    idx = idx + 1
    url = articles_crawler(i)
    if not url:
        break
    news_url.append(url)


def makeList(newlist, content):
    for i in content:
        for j in i:
            newlist.append(j)
    return newlist


news_url_1 = []

makeList(news_url_1, news_url)

final_urls = news_url_1

link = []
titles = []
authors = []
publish_date = []
text = []
top_image = []
movies = []
keywords = []
summary = []
idx = 0
for i in tqdm(final_urls):
    time.sleep(idx % 5)
    idx = idx + 1
    fail = False
    try:
        config = Config()
        config.browser_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        article = Article(i, config=config)
        article.download()
        article.parse()
        article.nlp()
    except:
        fail = True
    if fail:
        continue

    link.append(i)
    titles.append(article.title.replace('\n', ' '))
    authors.append(article.authors)
    publish_date.append(article.publish_date)
    text.append(article.text.replace('\n', ' '))
    top_image.append(article.top_image)
    movies.append(article.movies)
    keywords.append(article.keywords)
    summary.append(article.summary.replace('\n', ' '))

import pandas as pd

news_df = pd.DataFrame({'date': publish_date, 'title': titles, 'link': link, 'content': text,
                        'authors': authors, 'top_image': top_image, 'keywords': keywords, 'summary': summary})

news_df = news_df.drop_duplicates(subset='link', keep='first', ignore_index=True)

news_df.to_csv('%s_%s_%s.csv' % (search, date.strftime("%Y_%m_%d"), l), index=False)