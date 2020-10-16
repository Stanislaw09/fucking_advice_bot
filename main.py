from urllib.request import urlopen
import os, sys
from selenium import webdriver
from time import sleep
import cv2
import pytesseract
import numpy as np
import pdfkit

pytesseract.pytesseract.tesseract_cmd=...            # path to tesseract.exe
path_wkhtmltopdf=...                                 # path to wkhtmltopdf.exe
config=pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

def ImgReading(path):
    req=urlopen(path)
    arr=np.asarray(bytearray(req.read()), dtype=np.uint8)
    img=cv2.imdecode(arr, 0)

    cropped=img[200:950, 300:1200]

    text=pytesseract.image_to_string(cropped)
    return text

def createPdf(titleUrl, descriptionUrl):
    return '<div style="display: flex; page-break-before: always;"><img width=400px src='+titleUrl+'></img>'+'\n'+'<p style="font-weight: 400; font-size: 20px; padding: 22px; line-height: 1.8em;">'+ImgReading(descriptionUrl)+'</p></div>'+'\n'


def getImages(username, password):
    driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
    pdf=''
    driver.get('https://instagram.com')
    sleep(2.2)
    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    sleep(2.2)
    driver.find_element_by_xpath("//button[contains(text(), 'Accept')]").click()
    driver.find_element_by_xpath("//button[@type='submit']").click()
    sleep(3.2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2.2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(1.5)
    driver.find_element_by_class_name('XTCLo.x3qfX').send_keys('good fucking advice')
    sleep(1.5)
    driver.find_element_by_class_name('z556c').click()
    sleep(3.2)

    posts=driver.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')

    sleep(1.5)

    for i in range(4):
        posts[i].click()
        sleep(1.6)
        container=driver.find_element_by_class_name('_97aPb')
        sleep(0.8)
        images=container.find_elements_by_class_name('FFVAD')

        pdf+=createPdf(images[0].get_attribute('src'), images[1].get_attribute('src'))

        close_div=driver.find_element_by_class_name('Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG')
        close_div.find_element_by_class_name('wpO6b').send_keys('\n')
        sleep(1.2)

    sleep(1)

    file=open('index.html', 'x')
    file.write(pdf)
    file.close()

    pdfkit.from_file('index.html', 'good_fucking_advice.pdf', configuration=config)


getImages(
#email,
#password
)
