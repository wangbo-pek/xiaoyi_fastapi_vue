from BackEnd.app.core.database import Base, engine
from BackEnd.app import models

def init_db():
    print('正在初始化数据库')
    Base.metadata.create_all(bind=engine)
    print('初始化成功')

if __name__ == '__main__':
    pass