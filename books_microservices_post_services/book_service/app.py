from flask import Flask


app = Flask(__name__)


from book_service.config.extentions import db
from book_service.models import *
from book_service.api.routers import *

if __name__ == '__main__':
    app.init_app(db)
    app.run(port=5000, debug=True)

