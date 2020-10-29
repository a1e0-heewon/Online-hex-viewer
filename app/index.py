from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
      return render_template('index.html')
    
@main.route('/upload', methods=['GET'])
def upload():
      return render_template('upload.html')