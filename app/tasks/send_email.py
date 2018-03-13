from datetime import datetime
from app.engines import db
from app.models import Job
from app.services.mail_service import MailService
from app.config import load_config
from app.tasks.task import Task


class SendMail(Task):
    def __init__(self, id_list, email_list):
        super().__init__('发送职位详情')
        self.id_list = id_list
        self.email_list = email_list

    def send_vulner_mail(self):
        contents = []
        vulners = db.session.query(Vulner).filter(Vulner.id.in_(self.id_list)).all()
        for vulner in vulners:
            contents.append(vulner.title)
        if len(contents) == 0:
            return
        config = load_config()
        with open('{}/app/resources/vulner_mail.html'.format(config.PROJECT_PATH)) as fp:
            mail_content = fp.read()
        mail_content = mail_content.replace('{{ content }}', "".join(contents))

        recipients = [email for email in self.email_list]

        mail_service = MailService()
        mail_service.send_mail(
            recipients=recipients,
            title='职位信息',
            content=mail_content
        )

    def process(self):
        self.send_vulner_mail()


if __name__ == "__main__":
    task = SendMail([1234, 5555], ['917086506@qq.com'])
    task.process()
