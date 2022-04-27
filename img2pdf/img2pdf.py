# -*- coding: utf-8 -*-
# @Time: 2021/11/27 13:00
# @Author: Yezi Chen
# @File: img2pdf.py
# @Platform: PyCharm

import os
import PIL
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape

def genpdf(filename, pagesizes):
    pdf = canvas.Canvas(filename)
    pdf.setPageSize(pagesizes)
    return pdf


def saveImage2pdf (pdf, image, x, y, w, h):
    pdf.drawImage(image, x, y, w, h)
    pdf.showPage()


if __name__ == '__main__':
    pdf_size = (2480, 3508)
    my_pdf = genpdf('my_pdf.pdf', pdf_size)
    folder = 'img'
    filelist = os.listdir(folder)
    for filename in filelist:
        img = PIL.Image.open(folder + '/' + filename)
        img_w, img_h = img.size
        img_x = (landscape(pdf_size)[1]-img_w)/2
        img_y = (landscape(pdf_size)[0]-img_h)/2
        saveImage2pdf(my_pdf, folder+'/'+filename, img_x, img_y, img_w, img_h)
    my_pdf.save()

