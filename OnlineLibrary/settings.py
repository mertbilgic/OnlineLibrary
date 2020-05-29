from flask import Flask
from helpers.file_upload_helpers import *
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.config['UPLOAD_FOLDER'] = FileUpload.UPLOAD_FOLDER