import requests
import bs4
from logger import logger


@logger(file_path='logs.txt')
def habr_parser(keywords: list):
    headers = {
        'Cookie': '_ym_d=1649583634; _ym_uid=1649583634769817403; _ga=GA1.2.1084108911.1649583634; hl=ru; fl=ru; visited_articles=570078:566004:570016:227377:664538:99923:196382; _ym_isad=2; habr_web_home_feed=/all/; _gid=GA1.2.1694905082.1660156609; pmtimesig=[[1660161479433,0],[1660162525508,1046075]]',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua-mobile': '?0'
    }

    response = requests.get('https://habr.com/ru/all/', headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all(class_='tm-article-snippet')
    previews = []

    for article in articles:
        article_tag_h2 = article.find('h2')
        article_tag_a = article_tag_h2.find('a')
        article_tag_time = article.find('time')
        datetime = article_tag_time.attrs['title']
        href = article_tag_a.attrs['href']
        url = 'https://habr.com' + href
        preview = {
            'article_date': datetime,
            'article_title': article_tag_a.text,
            'article_url': url
        }
        previews.append(preview)
    articles_found = ''
    for preview in previews:
        response = requests.get(preview['article_url'], headers=headers)
        text = response.text
        soup = bs4.BeautifulSoup(text, features="html.parser")
        article = soup.find(class_='tm-article-presenter__content tm-article-presenter__content_narrow')
        for keyword in keywords:
            if keyword in article.text:
                data = f"{preview['article_date']}, '----->', {preview['article_title']}, '----->', {preview['article_url']}\n"
                if data not in articles_found:
                    articles_found += data
    return f"Cтатьи, содержащие ключевые слова {keywords} в формате: <дата> - <заголовок> - <ссылка>:\n" \
           f"{articles_found}"
