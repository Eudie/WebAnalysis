#!/usr/bin/python
# Author: Eudie

import pandas as pd
import json
import codecs
from eventregistry import *

page_num = 1
res = {'articles':{'pages': 10000000}}
while True:
    er = EventRegistry()
    er.login(username="Eudie", password="StudyHard1!")
    q = QueryArticles(lang="eng")

    # find articles mentioning the company Fitness
    #q.addConcept(er.getConceptUri("Fitness"))
    q.addCategory(er.getCategoryUri("Fitness"))

    # return the list of top 5 articles, including the concepts, categories and article image
    q.addRequestedResult(RequestArticlesInfo(page = page_num, count = 200,
        returnInfo=ReturnInfo(articleInfo=ArticleInfoFlags(concepts=True, categories=True))))
    if(page_num > res['articles']['pages']):
        break

    res = er.execQuery(q)

    with codecs.open('Fitness/eventRegistry_' + str(page_num) + '.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)

    page_num += 1
