import requests
import time
from app.logger import ContextLogger
from app.engines import db

class BaseReq:
    def __init__(self, is_crawl=True):
        self.ses = db.session
        self.is_crawl = is_crawl
        self.logger = ContextLogger('crawl')
        self.headers = {
            'Host': 'www.lagou.com',
            'Upgrade - Insecure - Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://www.lagou.com/jobs/list_Python?px=new&city=%E5%85%A8%E5%9B%BD',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'multipart/form-data'
        }

    def _request(self, url, method='post', timeout=20, retry=5, **kwargs):

        if kwargs.get('cookies'):
            cookies = kwargs['cookies']
        else:
            cookies = {}
        try:
            resp = requests.request(method, '{}'.format(url), timeout=timeout, headers=self.headers,
                                    cookies=cookies, **kwargs)
        except Exception as e:
            if retry > 0:
                return self._request(url, method, timeout, retry=retry-1, **kwargs)
            else:
                self.logger.warning('请求失败', e)
                return None
        if resp.status_code != 200 and retry > 0:
            return self._request(url, method, timeout, retry=retry-1, **kwargs)
        if self.is_crawl:

            return resp.text
        else:
            try:
                data = resp.json()
                if (data['success'] is False or data is None) and retry > 0:
                    time.sleep(3)
                    return self._request(url, method, timeout, retry=retry - 1, **kwargs)
            except Exception as e:
                if retry > 0:
                    return self._request(url, method, timeout, retry=retry - 1, **kwargs)
                else:
                    self.logger.warning('解析失败', e)
                    self.logger.warning(url)
                    data = None
            return data

    def get(self, url, **kwargs):
        return self._request(url, method='get', **kwargs)

    def post(self, url, **kwargs):
        return self._request(url, method='post', **kwargs)

