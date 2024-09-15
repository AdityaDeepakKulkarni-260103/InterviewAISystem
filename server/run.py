from app import create_app,db
from flask_migrate import Migrate
from app.config import condfig_dict
from dotenv import load_dotenv
import os

DEBUG = (os.getenv("DEBUG", ' False') == 'True')
load_dotenv()
get_config = 'Debug' if DEBUG else "Production"
try:
    app_config = condfig_dict[get_config]
except KeyError:
    print("Config is inavalid")

app = create_app(app_config)
Migrate(app,db)

if DEBUG:
    app.logger.info("DBMS = "+app_config.SQLALCHEMY_DATABASE_URI)
if __name__ == "__main__":
    app.run(debug=True)