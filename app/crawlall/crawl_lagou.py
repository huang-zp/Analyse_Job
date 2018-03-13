import pandas as pd  # 数据框操作
import requests  # 网络请求
import re
import time
import random

# post的网址
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'

# 反爬措施
header = {'Host': 'www.lagou.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
          'Accept-Encoding': 'gzip, deflate, br',
          'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'X-Requested-With': 'XMLHttpRequest',
          'X-Anit-Forge-Token': 'None',
          'X-Anit-Forge-Code': '0',
          'Content-Length': '26',
          'Cookie': 'user_trace_token=20171103191801-9206e24f-9ca2-40ab-95a3-23947c0b972a; _ga=GA1.2.545192972.1509707889; LGUID=20171103191805-a9838dac-c088-11e7-9704-5254005c3644; JSESSIONID=ABAAABAACDBABJB2EE720304E451B2CEFA1723CE83F19CC; _gat=1; LGSID=20171228225143-9edb51dd-ebde-11e7-b670-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKkJPgBHAnny1nUKaLpx2oDfUXv9ItIF3kBAWM2-fDNu%26ck%3D3065.1.126.376.140.374.139.129%26shh%3Dwww.baidu.com%26sht%3Dmonline_3_dg%26wd%3D%26eqid%3Db0ec59d100013c7f000000055a4504f6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20171228225224-b6cc7abd-ebde-11e7-9f67-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=3ec21cea985a4a5fa2ab279d868560c8',
          'Connection': 'keep-alive',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache'}

for n in range(30):
    # 要提交的数据
    form = {'first': 'false',
            'kd': 'Python',
            'pn': str(n)}

    time.sleep(random.randint(2, 5))

    # 提交数据
    html = requests.post(url, data=form, headers=header)
    print(html.text)


