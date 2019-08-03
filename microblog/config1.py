import os


class Config1(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
