from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from werkzeug import secure_filename

upload = Blueprint('upload', __name__, url_prefix='/')

@upload.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('./file/' + secure_filename(f.filename))
      return render_template('index.html')