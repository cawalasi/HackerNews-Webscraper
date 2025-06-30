import requests
from bs4 import BeautifulSoup
url = 'https://news.ycombinator.com/news'



titles = []
links = []




def get_titles(soup):
    title = soup.select('td[class="title"]')
    for t in range (len(title)):
        if t % 2 == 1:
            titles.append(title[t].text)
    return titles
if __name__ == "__main__":
    for i in range(1,4):
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        title = get_titles(soup)
        url = 'https://news.ycombinator.com/news?p=' + str(i+1)

    for t in range(len(titles)):
        print(f'{t}: {titles[t]}')

    


