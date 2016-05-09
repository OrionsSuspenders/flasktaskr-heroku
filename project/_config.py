# project/_config.py

import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
DEBUG = False
SECRET_KEY = '12c4f03d87f21f 10c254b2dbca8a 1f9ff4a2ce73e1 716cb6d8e73abf 5ec7bb160df49d\
                c31d096e2ee144 49b26def6e4bb0 57a4abdf94920f 96ccb5b633148a e0a1b9e43f5c31\
                f7f5c51f4d8541 0a046bb06c653a 8f473153468763 df9815d7c22300 7fdd82f5918279\
                2c48831b60416e 1ac7666241e023 444b3b84c9f817 f49aba6385ae27 94e01c35e3d104\
                8232f3c19d48e2 875197c19460cf e43c32981c6910 bc7eba51f3e780 fe5200fd25f5c0\
                7180b597d6fe20 49f2e2a7fbdf4d 22718753260964 21a39aa5b310cc e0fa9133ab95f8\
                d51f70f3d4e458 b1620a05fcad1d bd1eeb361cf1cd 8a49ef9d5bbe71 ed63de327224fe\
                5ab5125096b4fc 497adbf140d431 7f4a0a1211e33d cd25e9f477f899 532e60b94df16d'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database url
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH