from app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models.base import Base

app = create_app()
migrate = Migrate(app, Base)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# 项目启动
if __name__ == "__main__":
    manager.run()
