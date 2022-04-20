from pdf2image import convert_from_path
import os


from pdf2image.exceptions import(
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


# path_pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
# path_pdf2img = path_pictures + "\\pdf2images\\"


path_pdf2img = 'UNpdf/pdf2img/'

file = 'test.pdf'

def pdf2img():

    if not os.path.exists(path_pdf2img):
        os.makedirs(path_pdf2img)

    
    pages = convert_from_path(file, 500)
    counter = 1
    for page in pages:
        myfile = path_pdf2img + 'output' + str(counter) + '.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")

    return path_pdf2img