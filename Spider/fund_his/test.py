url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18305786680500915409_1598786181832&fundCode=004453&pageIndex=3&pageSize=20&startDate=&endDate=&_=1598786263322'
import requests

r = requests.get(url)
print(r.text)

