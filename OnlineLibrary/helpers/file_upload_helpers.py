
import os
from werkzeug.utils import secure_filename
class FileUpload:
    UPLOAD_FOLDER = 'static/img/'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    FILE_NAME = ''
    
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in FileUpload.ALLOWED_EXTENSIONS