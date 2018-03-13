import os
from datetime import timedelta, datetime
from app.models import Job
from app.engines import db

from app.logger import ContextLogger
from app.tasks.task import Task

FILE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/app/resources/' + 'index.txt'

now = datetime.now().strftime("%Y-%m-%d")
end_time = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")


class CrawlFreebuf(Task):
    def __init__(self):
        super().__init__('LaGou数据爬取')
        self.logger = ContextLogger('task_lagou')
        self.is_crawl = False
        self.end_time = db.session.query(Job).order_by(Job.createTime.desc()).first().createTime
        self.headers = {
            'Host': 'www.lagou.com',
            'Upgrade - Insecure - Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://www.lagou.com/jobs/list_Python?px=new&city=%E5%85%A8%E5%9B%BD',
            'Connection': 'keep-alive',
            'Cookie': 'user_trace_token=20171103191801-9206e24f-9ca2-40ab-95a3-23947c0b972a; _ga=GA1.2.545192972.1509707889; LGUID=20171103191805-a9838dac-c088-11e7-9704-5254005c3644; JSESSIONID=ABAAABAACDBABJB2EE720304E451B2CEFA1723CE83F19CC; _gat=1; LGSID=20171228225143-9edb51dd-ebde-11e7-b670-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKkJPgBHAnny1nUKaLpx2oDfUXv9ItIF3kBAWM2-fDNu%26ck%3D3065.1.126.376.140.374.139.129%26shh%3Dwww.baidu.com%26sht%3Dmonline_3_dg%26wd%3D%26eqid%3Db0ec59d100013c7f000000055a4504f6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20171228225224-b6cc7abd-ebde-11e7-9f67-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=3ec21cea985a4a5fa2ab279d868560c8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Anit-Forge-Token': 'None',
            'X-Anit-Forge-Code': '0',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

    def process(self, page, tag):

        base_url = 'https://www.lagou.com/jobs/positionAjax.json?'
        params = {
            'px': 'new',
            'needAddtionalResult': 'false',
            'isSchoolJob': '0'
        }
        data = {
            'first': 'false',
            'pn': str(page),
            'kd': tag
        }
        html = self.post(base_url, data=data, params=params)

        if html:
            try:
                count = int(html['content']['positionResult']['resultSize'])
                job_list = html['content']['positionResult']['result']
                if count == 0:
                    return True
                for job in job_list:
                    result = self.storage(job, tag)
                    if result:
                        return True
            except Exception as e:
                self.logger.warning('取值失败', e)
                self.logger.warning(base_url)
        return False

    def storage(self, job_dict, tag):

        for key in job_dict:
            job_dict[key] = self.switch_str(job_dict[key])


        if job_dict['createTime'] <= self.end_time:
            return True
        job = Job()
        try:
            job.companyId = job_dict['companyId']
            job.positionName = job_dict['positionName']
            job.workYear = job_dict['workYear']
            job.education = job_dict['education']
            job.jobNature = job_dict['jobNature']
            job.companyLogo = job_dict['companyLogo']
            job.salary = job_dict['salary']
            job.city = job_dict['city']
            job.financeStage = job_dict['financeStage']
            job.industryField = job_dict['industryField']
            job.positionId = job_dict['positionId']
            job.approve = job_dict['approve']
            job.createTime = job_dict['createTime']
            job.positionAdvantage = job_dict['positionAdvantage']
            job.companySize = job_dict['companySize']
            job.companyLabelList = job_dict['companyLabelList']
            job.publisherId = job_dict['publisherId']
            job.score = job_dict['score']
            job.district = job_dict['district']
            job.companyShortName = job_dict['companyShortName']
            job.positionLables = job_dict['positionLables']
            job.industryLables = job_dict['industryLables']
            job.businessZones = job_dict['businessZones']
            job.longitude = job_dict['longitude']
            job.latitude = job_dict['latitude']
            job.adWord = job_dict['adWord']
            job.formatCreateTime = job_dict['formatCreateTime']
            job.hitags = job_dict['hitags']
            job.resumeProcessRate = job_dict['resumeProcessRate']
            job.resumeProcessDay = job_dict['resumeProcessDay']
            job.companyFullName = job_dict['companyFullName']
            job.imState = job_dict['imState']
            job.lastLogin = job_dict['lastLogin']
            job.explain = job_dict['explain']
            job.plus = job_dict['plus']
            job.pcShow = job_dict['pcShow']
            job.appShow = job_dict['appShow']
            job.deliver = job_dict['deliver']
            job.gradeDescription = job_dict['gradeDescription']
            job.promotionScoreExplain = job_dict['promotionScoreExplain']
            job.firstType = job_dict['firstType']
            job.secondType = job_dict['secondType']
            job.isSchoolJob = job_dict['isSchoolJob']
            job.subwayline = job_dict['subwayline']
            job.stationname = job_dict['stationname']
            job.linestaion = job_dict['linestaion']
            job.job_type = tag
        except Exception as e:
            self.logger.warning('存储失败', e)
            self.logger.warning(job_dict['publisherId'])
#        self.logger.info(job_dict['positionName']+job_dict['createTime'])
        self.safe_commit(job)
        return False

    def switch_str(self, value_list):
        value_str = ''
        try:
            if type(value_list) != list:
                return str(value_list)

            for value in value_list:
                value_str = value_str + value + ';'
        except Exception as e:
            self.logger.warning('转化失败', e)
        return value_str

    def control(self):
        tag_list = []
        with open(FILE_PATH, 'r') as f:
            for line in f:
                tag_list.append(line.strip())
        for tag in tag_list:
            page = 1
            while(True):
                result = self.process(page, tag)
                if result:
                    break
                print("当前页数{}".format(page))
                page += 1
            self.logger.warning(tag+'共发起了'+str(page)+'请求')


if __name__ == "__main__":
    freebuf = CrawlFreebuf()
    freebuf.control()


