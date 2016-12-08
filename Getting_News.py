#!/usr/bin/python
# Author: Eudie

# import gnp
# import codecs
# import json
#
# d = gnp.get_google_news_query("Fitness tech")
#
#
# j = json.dumps(d, indent=4, ensure_ascii=False)
# f = codecs.open( 'news.json', 'w', encoding='utf-8')
# f.write(j.decode('utf-8'))
# f.close()
#
# from eventregistry import *
# er = EventRegistry()
# q = QueryEvents()
# q.addConcept(er.getConceptUri("Fitness"))
# q.addRequestedResult(RequestEventsInfo(sortBy = "date", count=1))   # return event details for last 10 events
# print er.execQuery(q)

from eventregistry import *
er = EventRegistry()
q = QueryArticles()
# set the date limit of interest
q.setDateLimit(datetime.date(2014, 4, 16), datetime.date(2014, 4, 28))
# find articles mentioning the company Apple
q.addConcept(er.getConceptUri("Apple"))
# return the list of top 30 articles, including the concepts, categories and article image
q.addRequestedResult(RequestArticlesInfo(page = 1, count = 30,
    returnInfo = ReturnInfo(articleInfo = ArticleInfoFlags(concepts = True, categories = True, image = True))))
res = er.execQuery(q)
print res