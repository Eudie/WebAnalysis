#!/usr/bin/python
# Author: Eudie

import pandas as pd
import json
import codecs
from pandas.io.json import json_normalize
from eventregistry import *

df = pd.DataFrame([])

list_of_json_files = ["Fitness/eventRegistry_2.json"]


for files in list_of_json_files:
    with codecs.open(files, "r", encoding='utf-8') as data_file:
        data = json.load(data_file)

    df = df.append(json_normalize(data['articles']['results']))


full_news_article = []
for article_uri in df['uri']:
    er = EventRegistry()
    er.login(username="Eudie", password="StudyHard1!")
    q = QueryArticle(article_uri)
    # get core article information
    q.addRequestedResult(RequestArticleInfo())
    res = er.execQuery(q)
    full_news_article.append(res[article_uri]["info"]["body"])

df['full_news_article'] = full_news_article

df = df.replace({'\n': ' ', '\t': ' ', '[|]': ' '}, regex=True)

writer = pd.ExcelWriter('EventRegistry_full_2.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index=False)




