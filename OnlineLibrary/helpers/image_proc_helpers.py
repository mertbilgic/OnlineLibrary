#https://nanonets.com/blog/ocr-with-tesseract/
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import re
class ImageProc:
    def __init__(self, image_path):
        self.image_path = image_path
        self.result = ''
        self.image = None

    def imread_image(self):
        self.image =  plt.imread(self.image_path)

    def imwrite_image(self):
        cv2.imwrite(self.image_path, self.image)

    def proc_image(self):
        # get grayscale image
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def read_image(self):
        self.result = pytesseract.image_to_string(Image.open(self.image_path))
    
    def get_isbn(self):
        #isbn = re.compile("(?:[0-9]{3}-)?[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,6}-[0-9]")
        #isbn = isbn.findall(self.result)
        space = self.result.find(' ')
        if space == -1 : space = 0 
        first_line = self.result.find('\n')
        isbn = self.result[space:first_line]
        isbn = re.sub(r'[^\w]', '', isbn)
        return isbn

         
    def get_result(self):
       self.imread_image()
       self.proc_image()
       self.imwrite_image()
       self.read_image()
       
       return self.get_isbn()
