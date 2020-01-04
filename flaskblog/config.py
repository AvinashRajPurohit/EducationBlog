import os
class Config:
    SECRET_KEY ='a34d0c212fe137ab1e1b93864a673a7a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL')
    MAIL_PASSWORD = os.environ.get('PASS')
