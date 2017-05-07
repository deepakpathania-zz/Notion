import time

import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'efd55592'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'c1a124c24951690cf61f9fcebc4842f1'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

opts = {
  'title': 'trump',
  'sort_by': 'relevance',
  'source_locations_country': ['IN'],
  'language': ['en'],
  'published_at_start': 'NOW-60DAYS',
  'published_at_end': 'NOW',
  'cursor': '*',
  'per_page': 100
}


def get_article(word):
    
    try:
        # List stories
        opts['title'] = word
        api_response = api_instance.list_stories(**opts)
        print("API called successfully. Returned data: ")
        print("========================================")
        for story in api_response.stories:
          print(story.title + " / " + story.source.name)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)

articles = get_article('aadhar')
print len(articles)
print articles[0]