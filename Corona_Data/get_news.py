from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
from newspaper import Article, Config # 뉴스 홈페이지가 달라도 제목과 본문을 추출할수 있도록 도와주는 라이브러리임
from urllib.parse import quote_plus
import pandas as pd
import datetime
import nltk
from user_agent import generate_user_agent
import time
from stem import Signal
from stem.control import Controller
from selenium import webdriver # 사용하는 라이브러리가 다름
import stem.process




def make_datelist():
    date_lists = []
    today = datetime.datetime.now()
    today = today.strftime("%Y-%m-%d")

    target_date = datetime.datetime(2021, 12, 7, 1, 35, 42, 657813)

    while(1):
        target_date = target_date + datetime.timedelta(days=1)
        str_target_date = target_date.strftime("%Y-%m-%d")
        date_lists.append(str_target_date)
        if today == str_target_date:
            break
    return date_lists

def make_newsfile(lang, search, page, page2, date, l, ipiter, controller):
    def makePgNum(num):
        if num == 1:
            return num - 1
        elif num == 0:
            return num
        else:
            return 10*(num-1)


    def makeUrl(search, date, language, start_pg, end_pg):
        if start_pg == end_pg:
            start_page = makePgNum(start_pg)
            url = "https://www.google.com/search?q=%s&tbs=cdr:1,cd_min:%s,cd_max:%s&tbm=nws&start=%s&lr=%s" \
             % (quote_plus(search), quote_plus(date.strftime("%m/%d/%Y")), quote_plus(date.strftime("%m/%d/%Y")),
             start_page, language)
            return url

    # lr -> 언어, cd_min, cd_max - > 날짜 시작 끝일 지정

        else:
            urls = []
            for i in range(start_pg, end_pg + 1):
                page = makePgNum(i)
                url = "https://www.google.com/search?q=%s&tbs=cdr:1,cd_min:%s,cd_max:%s&tbm=nws&start=%s&lr=%s" \
             % (quote_plus(search), quote_plus(date.strftime("%m/%d/%Y")), quote_plus(date.strftime("%m/%d/%Y")),
             page, language)
                urls.append(url)
            return urls


    def news_attrs_crawler(articles,attrs):
        attrs_content=[]
        for i in articles:
            attrs_content.append(i.attrs[attrs])
        return attrs_content

    a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    headers = {"User-Agent": a}
    # 사람이 접속했다는 표시를 내기위함
    # user agent string을 검색 -> 무엇이 나왔는지 확인하고 복사해서 사용하면 됨.


    def articles_crawler(url, ipiter, controller):

        try:
            # ip address changing
            #controller.authenticate('ss2959')
            #controller.signal(Signal.NEWNYM)
            #print(ipiter)
            #if ipiter == 0 and (controller.is_newnym_available() == False):
            #    print("ip 주소변경")
            #    print("waiting for Tor to change IP: " + str(controller.get_newnym_wait()) + " sec")
            #    time.sleep(controller.get_newnym_wait())

            options = webdriver.ChromeOptions()
            #hostname = "socks5://127.0.0.1"
            #port = "9050"
            #options.add_argument('--proxy-server=%s' % hostname + ":" + port)
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            navigator = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
            options.add_argument("user-agent=" + navigator)
            driver = webdriver.Chrome('./chromedriver', chrome_options=options)
            # 크롬 드라이버를 설치해야함
            # 버전에 맞는 드라이버를 다운.
            driver.get(url)
            driver.implicitly_wait(10)
            time.sleep(0.7)
            # 데이터가 로드될때 까지 기다림.
            html = driver.page_source
            html = BeautifulSoup(html, "html.parser") #
            url_google = html.select("#rso > div > div > div > div > div > a")
            url = news_attrs_crawler(url_google,'href')
            driver.quit()

        except:
            url = []
        return url

    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    url = makeUrl(search,date,lang[l],page,page2)


    news_titles = []
    news_url =[]
    news_contents =[]
    news_dates = []
    idx = 1
    for i in url:
        #if len(url) < 15:
        #    time.sleep(10)
        time.sleep(idx % 5)
        idx = idx + 1
        url = articles_crawler(i, ipiter, controller)
        if not url:
            break
        news_url.append(url)


    def makeList(newlist, content):
        for i in content:
            for j in i:
                newlist.append(j)
        return newlist



    news_url_1 = []


    makeList(news_url_1,news_url)


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
        time.sleep(idx % 10)
        idx = idx + 1
        fail = False
        try:
            config = Config()
            config.browser_user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
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
        time.sleep(5)


    news_df = pd.DataFrame({'date':publish_date,'title':titles,'link':link,'content':text,
                            'authors':authors, 'top_image':top_image, 'keywords':keywords, 'summary':summary})

    news_df = news_df.drop_duplicates(subset='link', keep='first',ignore_index=True)

    filename = "Covid_19"
    datapath = "/media/suseong/One Touch/CoronaData/"
    datapath = datapath + '%s_%s_%s.csv' % (filename, date.strftime("%Y_%m_%d"), l)
    news_df.to_csv(datapath ,index=False)

if __name__ == "__main__":
    """tor_process = stem.process.launch_tor_with_config(tor_cmd="/etc/default/tor", config={
        'SOCKSPort': "9050",
        'ControlPort': "9051",
        'ExitNodes': '{kr}',
        'GeoIPFile': "/usr/share/tor/geoip",
        'GeoIPv6File': "/usr/share/tor/geoip6"
    }
    )"""
    with Controller.from_port(port=9051) as controller:
        nltk.download("punkt")
        date_lists = make_datelist()
        #search = input("검색어 입력: ")
        lang = {'korean': 'lang_ko', 'english': 'lang_en', 'spanish': 'lang_es', 'french': 'lang_fr', 'italiano': 'lang_it'}
        search = '코로나19 OR "신종 코로나" OR "코로나 바이러스" OR "신종 코로나바이러스" OR COVID-19 OR 코비드19 OR 우한폐렴'
        page = 1
        page2 = 10
        l = 'korean'
        a = generate_user_agent(os = 'win', device_type='desktop')
        print(a)
        idx = 0
        for index, date in enumerate(date_lists):
            print("첫번째 idx = %d" % idx)
            make_newsfile(lang, search, page, page2, date, l, idx, controller)
            idx += 1
            if (idx >= 20):
                idx = 0
    controller.close()