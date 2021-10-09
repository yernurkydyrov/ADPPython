from scraper import news

if __name__ == '__main__':
    scrapper = news()
    # We are getting articles
    # and inside the article there are paragraphs of text
    articles = scrapper.getNews("bitcoin",1)
    for n in articles[0]:
        print(n)
