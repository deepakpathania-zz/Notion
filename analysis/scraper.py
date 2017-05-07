import time
from collections import defaultdict
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'efd55592'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'c1a124c24951690cf61f9fcebc4842f1'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

def get_all_stories(word):
  params = {
    'title': word,
    'sort_by': 'relevance',
    'source_locations_country': ['IN'],
    'language': ['en'],
    'published_at_start': 'NOW-60DAYS',
    'published_at_end': 'NOW',
    'cursor': '*',
    'per_page': 100
  }

  fetched_stories = []
  stories = None
  
  while stories is None or len(stories) > 0:
    try:
      response = api_instance.list_stories(**params)
    except ApiException as e:
      if ( e.status == 429 ):
        print('Usage limit are exceeded. Wating for 60 seconds...')
        time.sleep(60)
        continue
        
    stories = response.stories
    params['cursor'] = response.next_page_cursor
    
    fetched_stories += stories
    print("Fetched %d stories. Total story count so far: %d" %
      (len(stories), len(fetched_stories)))
     
  return fetched_stories

articles = get_all_stories('aadhar')
print len(articles)
# print articles[0]

news_list = {}

for article in articles:
  news = {}
  nid = article.id
  news_list[nid] = news
  news['id'] = nid
  news['title'] = article.title
  news['summary'] = '\n'.join(article.summary.sentences)
  news['body'] = article.body
  news['url'] = article.links.permalink
  news['date'] = article.published_at.strftime('%d/%m/%Y %H:%M')
  news['keywords'] = article.keywords
  news['sentiment'] = article.sentiment.body.polarity

print news_list[news_list.keys()[0]]

import json
with open('result.json', 'w') as fp:
    json.dump(news_list, fp, indent=4, sort_keys=True)


