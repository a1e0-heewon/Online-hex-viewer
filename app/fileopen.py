from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from werkzeug import secure_filename
import os

fileopen = Blueprint('fileopen', __name__, url_prefix='/')

@fileopen.route('/fileOpen', methods = ['GET', 'POST'])
def open_file():
    path = "./file/"
    file_list = os.listdir(path)
    print (file_list)
    
    return render_template('filelist.html', lists=file_list)