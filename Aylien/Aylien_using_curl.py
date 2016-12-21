# import requests
# import json
# # url = "https://api.newsapi.aylien.com/api/v1/stories?language%5B%5D=en&published_at.start=NOW-3HOUR&published_at.end=NOW&categories.taxonomy=iptc-subjectcode&categories.confident=true&categories.id%5B%5D=07016000&cluster=false&cluster.algorithm=lingo&sort_by=published_at&sort_direction=desc&cursor=*&per_page=10"
# # data = requests.get(url).json
# # print data
# #
# #
# # curl -X GET --header "Accept: application/json" --header "X-AYLIEN-NewsAPI-Application-ID: e8d39be3" --header "X-AYLIEN-NewsAPI-Application-Key: b693f631923fd42de6901ae725224e8b"
#
# url = "https://api.newsapi.aylien.com/api/v1/stories?language%5B%5D=en&published_at.start=NOW-3HOUR&published_at.end=NOW&categories.taxonomy=iptc-subjectcode&categories.confident=true&categories.id%5B%5D=07016000&cluster=false&cluster.algorithm=lingo&sort_by=published_at&sort_direction=desc&cursor=*&per_page=10"
#
# headers = {"Accept: application/json", "X-AYLIEN-NewsAPI-Application-ID: e8d39be3", "X-AYLIEN-NewsAPI-Application-Key: b693f631923fd42de6901ae725224e8b"}
# r = requests.get(url, headers=headers).json()
# print r


import urllib2

url = "https://api.newsapi.aylien.com/api/v1/stories?language%5B%5D=en&published_at.start=NOW-3HOUR&published_at.end=NOW&categories.taxonomy=iptc-subjectcode&categories.confident=true&categories.id%5B%5D=07016000&cluster=false&cluster.algorithm=lingo&sort_by=published_at&sort_direction=desc&cursor=*&per_page=10"
req = urllib2.Request(url, {"Accept: application/json", "X-AYLIEN-NewsAPI-Application-ID: e8d39be3", "X-AYLIEN-NewsAPI-Application-Key: b693f631923fd42de6901ae725224e8b"})
print req
f = urllib2.urlopen(req)
for x in f:
    print(x)
f.close()
