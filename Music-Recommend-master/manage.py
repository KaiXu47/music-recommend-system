import random

from flask import Flask
import os
import sys
from Src.App.views import blue, recommend
from Src.App.ext import StdError
from Src.App.models import UploadMusic
import schedule
import time

app = Flask(__name__, template_folder='Src/Template', static_folder='Src/Static',
            root_path=os.path.dirname(os.path.abspath(__file__)))
app.register_blueprint(blueprint=blue)

if __name__ == "__main__":

    # um = UploadMusic()
    # um.import_scrapy_data()
    recommend.calculate()
    StdError.info("app_name:" + str(app.name))
    StdError.info("root_path:" + str(app.root_path))
    StdError.info("template_folder:" + str(app.template_folder))
    StdError.info("static_folder:" + str(app.static_folder))
    app.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
    recommend.save_model()