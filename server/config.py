
class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config): #기본설정 그대로
    pass

class TestConfig(Config): #테스팅환경
    TESTING = True

class DebugConfig(Config): #개발모드
    DEBUG = True