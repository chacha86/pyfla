import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql://testUser:1234@test.chacha.world:3306/b3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"