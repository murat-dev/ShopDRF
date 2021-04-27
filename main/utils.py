import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    return response.text

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='css-1a6p917').find('div', class_='MuiGrid-root').find('div', class_='MuiGrid-container')
    all_pages = pages.find_all('div', class_='MuiGrid-item')

    news = []

    for line in all_pages:
        try:
            title = line.find('div', class_='css-1o97fzj').find('h2').text
        except:
            title = ''
        try:
            description = line.find('div', class_='css-1o97fzj').find('p').text
        except:
            description = ''

        if title == '':
            continue

        data = {
            'title': title,
            'description': description,
        }

        news.append(data)

    return news

def main():
    url = 'https://fashionunited.com/news/fashion'
    return get_page_data(get_html(url))

