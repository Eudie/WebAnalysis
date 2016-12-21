#!/usr/bin/python
# Author: Eudie

import aylien_news_api
import json
import codecs
from aylien_news_api.rest import ApiException


aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'e8d39be3'
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'b693f631923fd42de6901ae725224e8b'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

language = ['en']
since = 'NOW-30DAY'
until = 'NOW'
categories_taxonomy = 'iptc-subjectcode'
categories_id = ['07016000']



try:
    # List stories
    api_response = api_instance.list_stories(language=language,
                                             published_at_start=since,
                                             published_at_end=until,
                                             categories_taxonomy=categories_taxonomy,
                                             categories_id=categories_id,
                                             per_page=100)

    # with codecs.open('Aylien.json', 'w', encoding='utf-8') as f:
    #     json.dumps(api_response.__dict__, f, ensure_ascii=False, indent=4)
    print api_response.stories[1].body
    print len(api_response.stories)
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %s\n" % e)
