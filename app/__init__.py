from flask import Flask

app = Flask(__name__)
from app.index import main as main
from app.fileupload import upload as upload
from app.hexview import hexv as hexv
from app.fileopen import fileopen as fileopen

app.register_blueprint(main)
app.register_blueprint(upload)
app.register_blueprint(hexv)
app.register_blueprint(fileopen)