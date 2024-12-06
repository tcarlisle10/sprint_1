import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Migmaster10!@localhost/trade_x_change'
    DEBUG = True


class TextingConfig:
    pass

class ProductionConfig:
    pass