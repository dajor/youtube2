from pytrends.request import TrendReq

pytrends1 = TrendReq(hl='de-DEU', tz=360)

print (pytrends1.suggestions(keyword='pizza'))


print (pytrends1.related_topics())

categories=pytrends1.categories()

print (type(categories))