

import os


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32))

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True


config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig
}