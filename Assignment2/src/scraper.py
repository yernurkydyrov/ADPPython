import requests
from bs4 import BeautifulSoup
import json
from newspaper import Article

class news:
    @classmethod
    def getCoinId(self, coinName):
        coinRequest = requests.get('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail?slug='+str(coinName)+'&langCode=en&aux=status')
        idSoup = BeautifulSoup(coinRequest.text, 'lxml')
        id_json = json.loads(idSoup.text)
        coinId = str(id_json['data']['id'])
        return coinId

    @classmethod
    def getNews(self,nameOfCoin,numberOfArticles):
        coinId = self.getCoinId(nameOfCoin)
        site = requests.get('https://api.coinmarketcap.com/content/v3/'
                            'news?coins='+coinId+'&page=1&size='+str(numberOfArticles))
        soup = BeautifulSoup(site.text, 'lxml')
        site_json = json.loads(soup.text)
        articles = []
        for slug in site_json['data'] :
            url = slug['meta']['sourceUrl']
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            articles.append(article.text.split('\n\n'))
        
        return articles


        


