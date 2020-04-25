import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time

class NYTScraper():
    
    def __init__(self):
        # url definition
        self.url = "https://www.nytimes.com/"

        # Request
        r1 = requests.get(self.url)
        print('Request status code: {}'.format(r1.status_code))

        # We'll save in coverpage the cover page content
        coverpage = r1.content

        # Soup creation
        soup1 = BeautifulSoup(coverpage, 'html5lib')

        # News identification
        self.coverpage_news = soup1.find_all('div', class_='css-6p6lnl')
        print('Number of articles found on cover page: {}\n'.format(len(self.coverpage_news)))

    def scrape_nyt(self, number_of_articles = 5):
        # Empty lists for content, links and titles
        news_contents = []
        list_links = []
        list_titles = []
        list_time = []

        for n in np.arange(0, number_of_articles):
            
            # Getting the link of the article
            link = 'https://www.nytimes.com' + self.coverpage_news[n].find('a')['href']
            list_links.append(link)
            
            # Retrieve article 
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')
            body = soup_article.select('section[class*="meteredContent"]')

            # Getting the title
            title = body[0].find('h1').get_text()
            list_titles.append(title)
            print('Link for article number {}: {}'.format(n,link))
            print('Title: {}'.format(title))
            
            # Reading the content (it is divided in paragraphs)
            paragraphs = body[0].find_all('p')
            
            # Get published time of article
            time_obj = soup_article.find('time')
            if time_obj.has_attr('datetime'):
                timestamp = time_obj['datetime']
            list_time.append(timestamp)
            print('Published on: {}'.format(timestamp))
            print('')
            
            # Unifying the paragraphs
            list_paragraphs = []
            for p in np.arange(0, len(paragraphs)):
                paragraph = paragraphs[p].get_text()
                list_paragraphs.append(paragraph)
                final_article = " ".join(list_paragraphs)
                
            news_contents.append(final_article)

        # create articles dictionary out of seperate lists
        articles = pd.DataFrame({
            'link': list_links,
            'time': list_time,
            'title': list_titles,
            'body': news_contents 
            })

        print(articles)

        return articles

if __name__ == "__main__":

    nyt_scraper = NYTScraper()

    nyt_scraper.scrape_nyt()