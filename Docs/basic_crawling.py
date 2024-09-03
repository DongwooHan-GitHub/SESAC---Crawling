import requests 
from bs4 import BeautifulSoup

def crawl_breaking_news_list():
    news_url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0014907888'

    response = requests.get(news_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        

        td = soup.find('td',{'class' : 'content'})

        for li in td.find_all('li'):
            try:
                if li['data-comment'] is not None:
                    a = li.find('a')
                    link = a['href']
                    text = a.text
                    print(link, text)
            except KeyError:
                pass

def crawl_ranking_news():
    ranking_url = 'https://news.naver.com/main/ranking/popularDay.naver'

    response = requests.get(ranking_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', {'class': 'rankingnews_box'})

        for article in articles:

            pressname = article.find('strong',{'class': 'rankingnews_name'}).text
            print(pressname)
            print('\n')

            # news = article.find('div',{'class' : 'rankingnews_list'})

            newstitles = article.find_all('li')
            for newstitle in newstitles:
                try:
                    a = newstitle.find('a')
                    newsname = a.text
                    newslink = a['href']
                    print(newsname)
                    print(newslink)
                    
                except :
                    pass
            print('\n')
            print("============")
            
        
            
            







        
        # for article in articles:
        #     try:
        #         a_tag = article.find('a')
        #         if a_tag:
        #             link = a_tag['href']
        #             text = a_tag.text.strip()
        #             print(link, text)
        #     except KeyError:
        #         pass
            
            
            
        

if __name__ == '__main__': 
    # crawl_breaking_news_list()
    crawl_ranking_news()
    