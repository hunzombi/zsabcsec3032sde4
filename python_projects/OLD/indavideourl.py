from bs4 import BeautifulSoup
import requests
import webbrowser


def get_link(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    mydivs = soup.find('body').find_all("iframe", {"title": "indavideo video player"})
    print(mydivs)
    video = mydivs[0]['src']
    return str(video)[:-12]
a = get_link(input("\n\n\n\n\nPlease Enter The Link: "))
webbrowser.open_new_tab(str(a))