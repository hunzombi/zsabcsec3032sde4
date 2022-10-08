import requests
from bs4 import BeautifulSoup

print('\n\n\n')
url = 'https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
unwanted = ['BBC World News TV', 'BBC World Service Radio',
            'News daily newsletter', 'Mobile app', 'Get in touch']

for news in headlines:
    if news.text.strip() not in unwanted:
        print(news.text.strip())