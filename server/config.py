

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:01cs0qxcl5k!@kbj-firstdb.cu8i1dwdnvpi.ap-northeast-2.rds.amazonaws.com/mysns"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config): #기본설정 그대로
    pass

class TestConfig(Config): #테스팅환경
    TESTING = True

class DebugConfig(Config): #개발모드
    DEBUG = True