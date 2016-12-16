#!/usr/bin/python
# Author: Eudie

import pandas as pd
import json
import codecs
from pandas.io.json import json_normalize

with codecs.open("eventRegistry1.json", "r", encoding='utf-8') as data_file:
    data = json.load(data_file)

print data['articles']['results'][0]['url']
print len(data['articles']['results'])

print json_normalize(data['articles']['results'])
