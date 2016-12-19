#!/usr/bin/python
# Author: Eudie

import pandas as pd
import json
import codecs
from pandas.io.json import json_normalize
from newspaper import Article

df = pd.DataFrame([])

list_of_json_files = ["eventRegistry3.json", "eventRegistry4.json"]


for files in list_of_json_files:
    with codecs.open(files, "r", encoding='utf-8') as data_file:
        data = json.load(data_file)

    df = df.append(json_normalize(data['articles']['results']))

full_news_article = []
summary = []
keywords_from_newspaper = []
for row in df['url']:
    news_main_article = Article(row)
    news_main_article.download()
    news_main_article.parse()
    full_news_article.append(news_main_article.text)

print full_news_article




