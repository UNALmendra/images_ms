import base64
from pdf2image import convert_from_bytes
import os
import requests
import pdf2image


from pdf2image.exceptions import(
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


# path_pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
# path_pdf2img = path_pictures + "\\pdf2images\\"


path_pdf2img = 'images_ms/UNpdf/pdf2img/'



def pdf2img(url: str, firstPage = None, lastPage=None):

    file = requests.get(url)

    if not os.path.exists(path_pdf2img):
        os.makedirs(path_pdf2img)

    img_file = []

    
    pages = convert_from_bytes(file.content, 500, first_page=firstPage, last_page=lastPage)
    counter = 1
    for page in pages:
        myfile = path_pdf2img + 'output' + str(counter) + '.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")
        with open(myfile, 'rb') as image:
            img_file.append(str(base64.b64encode(image.read())))


    return str(img_file)