import requests

resp = requests.request('get', 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=python&sb=1&sm=0&isfilter=0&fl=489&isadv=0&sg=0e48987408d24799b14e9053dd9a00c7&p=1')

print(resp)
print(resp.text)