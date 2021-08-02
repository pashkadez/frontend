import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or \
                 "oM7MRxcROCBYtIOdInC6DIBNro0OnfLyRZaNc"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
                              "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def getEnvVariable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected env variable {name} not set."
        raise Exception(message)


POSTGRES_HOST = getEnvVariable("POSTGRES_HOST")
POSTGRES_PORT = getEnvVariable("POSTGRES_PORT")
POSTGRES_USER = getEnvVariable("POSTGRES_USER")
POSTGRES_PW = getEnvVariable("POSTGRES_PW")
POSTGRES_DB = getEnvVariable("POSTGRES_DB")

RABBIT_HOST = getEnvVariable("RABBIT_HOST")
RABBIT_PORT = getEnvVariable("RABBIT_PORT")
RABBIT_USER = getEnvVariable("RABBIT_USER")
RABBIT_PW = getEnvVariable("RABBIT_PW")
RABBIT_QUEUE = getEnvVariable("RABBIT_QUEUE")


DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
