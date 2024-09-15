import os, random, string
from dotenv import load_dotenv
import sqlalchemy
import traceback

class Config(object):
    load_dotenv()
    BASEDIR  = os.path.join(os.path.abspath(os.path.dirname(__file__)),'..')
    SECRET_KEY = ''.join(random.choice(string.ascii_lowercase) for i in range (32))
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    OPENAI_API_TYPE = os.getenv('OPENAI_API_TYPE')
    OPENAI_RESOURCE_ENDPOINT = os.getenv('OPENAI_RESOURCE_ENDPOINT')
    OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION')
    OPENAI_GPT_ENGINE = os.getenv('OPENAI_GPT_ENGINE')

    VERCEL_BLOB_ACCT_NAME = os.getenv('VERCEL_BLOB_ACCT_NAME')
    VERCEL_BLOB_CONTAINER = os.getenv('VERCEL_BLOB_CONTAINER')
    VERCEL_BLOB_KEY = os.getenv('VERCEL_BLOB_KEY')

    DATABASE_USERNAME_LOCAL = os.getenv('DATABASE_USERNAME_LOCAL')
    DATABASE_PASS_LOCAL = os.getenv('DATABASE_PASS_LOCAL')
    DATABASE_HOST_LOCAL = os.getenv('DATABASE_HOST_LOCAL')
    DATABASE_NAME_LOCAL = os.getenv('DATABASE_NAME_LOCAL')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DATABASE_USERNAME_LOCAL}:{DATABASE_PASS_LOCAL}@{DATABASE_HOST_LOCAL}/{DATABASE_NAME_LOCAL}'

class DebugConfig(Config):
    DEBUG = True

condfig_dict = {
    'Debug':DebugConfig
}
    
