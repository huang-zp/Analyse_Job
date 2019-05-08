import sys
import requests
from app.engines import db
from app.logger import ContextLogger
from app.utill.req import BaseReq

# 基础的任务类
# 含有比如开始时间记录，结束时间记录，安全提交等函数
# 这样其他的任务继承这个基础任务就不同定义以上函数了
class Task(BaseReq):
    def __init__(self, name, time=None):
        super().__init__()
        self.logger = ContextLogger('task')
        self.name = name
        self.time = time
        self.cookies = {}
        self.headers = {}

    def start(self):
        self.logger.info("Task Started: {}".format(self.name))

    def exit(self):
        sys.exit()

    def finish(self):
        self.logger.info("Task Finished: {}".format(self.name))

    def run(self):
        self.start()
        self.run_crawl()
        self.finish()

    def safe_commit(self, value):
        try:
            db.session.add(value)
            db.session.commit()
            self.logger.info(value.job_type + value.createTime + '提交成功')
        except Exception as e:
            self.logger.warning(e)
            db.session.rollback()

    def get_one_page(self, url):
        """
        Crawl a url and return the HTML code for this url.

        Args:
            url: The url you need to crawl.

        Returns:
            the HTML code for this url
        """
        # try:
        #     response = requests.get(url, headers=self.headers)
        # except Exception as e:
        #     self.logger.warning(url + ' ' + str(e))
        #     return False
        # return response.text
        response = self.get(url)
        return response

    def run_crawl(self):
        """
        Traverse all the pages you need to crawl.
        """
        pass

    def handle_list_html(self, html, tag):
        """
        The analysis page gets all the urls you need to crawl.

        Args:
            html: The page HTML that needs to be analyzed
        """
        pass

    def handle_info_html(self, html, url, tag):
        """
        The analysis page extracts all vulnerability information and commit to database.

        Args:
            html: The page HTML that needs to be analyzed
            url: The page url that needs to be analyzed
        """
        pass



