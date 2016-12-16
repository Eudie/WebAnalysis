#!/usr/bin/python
# Author: Eudie

import pandas as pd
import json
import codecs
from eventregistry import *


er = EventRegistry()
er.login(username="Eudie", password="StudyHard1!")
q = QueryArticles()

# find articles mentioning the company Fitness
q.addConcept(er.getConceptUri("Fitness"))
# return the list of top 5 articles, including the concepts, categories and article image
q.addRequestedResult(RequestArticlesInfo(page = 1, count = 2,
    returnInfo=ReturnInfo(articleInfo=ArticleInfoFlags(concepts=True, categories=True, image=True))))
res = er.execQuery(q)

with codecs.open('eventRegistry1.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=4)

