#!/usr/bin/python
# Author: Eudie

import codecs
import json
import pycurl
from StringIO import StringIO
url = "https://api.newsapi.aylien.com/api/v1/stories?language%5B%5D=en&published_at.start=NOW-3HOUR&published_at.end=NOW&categories.taxonomy=iptc-subjectcode&categories.confident=true&categories.id%5B%5D=07016000&cluster=false&cluster.algorithm=lingo&sort_by=published_at&sort_direction=desc&cursor=*&per_page=10"

buffer = StringIO()
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.HTTPHEADER, ["Accept: application/json", "X-AYLIEN-NewsAPI-Application-ID: ", "X-AYLIEN-NewsAPI-Application-Key: "])
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = json.loads(buffer.getvalue())
print type(body)

with codecs.open('Aylien.json', 'w', encoding='utf-8') as f:
    json.dump(body, f, ensure_ascii=False, indent=4)


