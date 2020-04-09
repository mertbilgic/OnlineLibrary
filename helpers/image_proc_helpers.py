#https://nanonets.com/blog/ocr-with-tesseract/
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class ImageProc:
    def __init__(self, image_path):
        self.image_path = image_path
        self.result = dict()
        self.image = None

    def imread_image(self):
        self.image =  plt.imread(self.image_path)

    def imwrite_image(self):
        cv2.imwrite(self.image_path, self.image)

    def proc_image(self):
        # get grayscale image
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def read_image(self):
        text = pytesseract.image_to_string(Image.open(self.image_path))
        return text

    def get_result(self):
       self.imread_image()
       self.proc_image()
       self.write_image()
       result = self.read_image()
