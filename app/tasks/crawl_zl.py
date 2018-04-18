import re
import os
from datetime import timedelta, datetime

from app.engines import db
from app.models import ZlJob

from app.logger import ContextLogger
from app.tasks.task import Task
from bs4 import BeautifulSoup
now = datetime.now().strftime("%Y-%m-%d")
end_time = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

FILE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/app/resources/' + 'index.txt'



# 智联爬虫

class CrawlZJ(Task):
    def __init__(self):
        super().__init__('智联招聘数据爬取')
        self.logger = ContextLogger('task_zhilian')

    def run_crawl(self):
        tag_list = []
        with open(FILE_PATH, 'r') as f:
            for line in f:
                tag_list.append(line.strip().lower())
        for tag in tag_list:
            base_url1 = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw="'
            base_url2 = '&sb=1&sm=0&isfilter=0&fl=489&isadv=0&sg=0e48987408d24799b14e9053dd9a00c7&p='
            index = 1
            while index < 91:
                next_page = base_url1 + tag + base_url2 + str(index)
                html = self.get_one_page(next_page)
                if html:
                    result = self.handle_list_html(html, tag)
                    if result:
                        break
                index += 1

    def handle_list_html(self, html, tag):
        soup = BeautifulSoup(html, 'lxml')
        try:
            list_content = soup.find(class_="newlist_list_content").find_all("table")
        except Exception as e:
            self.logger.warning(e)
            return False
        for i, table in enumerate(list_content):
            if i == 0:
                continue
            try:
                position_url = table.tr.td.div.a['href']
                position_name = table.tr.td.div.a.get_text().strip()
            except Exception as e:
                self.logger.warning(e)
                return False
            if tag not in position_name.lower():
                return True
            html = self.get_one_page(position_url)
            if html:
                result = self.handle_info_html(html, position_url, tag)
                if result:
                    return result
        return False

    def handle_info_html(self, html, url, tag):
        soup = BeautifulSoup(html, 'lxml')
        try:
            url = url
            positionName = soup.find(class_="inner-left fl").h1.get_text().strip()
            companyFullName = soup.find(class_="inner-left fl").h2.get_text().strip()

            companyLabelList = ''
            for i in soup.find(class_="inner-left fl").div.find_all('span'):
                companyLabelList = companyLabelList + i.get_text().strip() + ';'

            list_attr = []
            for i in soup.find(class_="terminalpage-left").find(class_='terminal-ul clearfix').find_all('li'):
                list_attr.append(i.strong.get_text().strip())
        except Exception as e:
            self.logger.warning(url + ' ' + str(e))
            return False
        job = ZlJob()
        job.url = url
        job.positionName = positionName
        job.companyFullName = companyFullName
        job.companyLabelList = companyLabelList
        job.salary = list_attr[0]
        job.city = list_attr[1]
        job.createTime = list_attr[2]
        job.jobNature = list_attr[3]
        job.workYear = list_attr[4]
        job.education = list_attr[5]
        job.positionCount = list_attr[6]
        job.firstType = list_attr[7]
        job.job_type = tag

        self.safe_commit(job)
        return False


if __name__ == "__main__":
    freebuf = CrawlZJ()
    freebuf.run()


