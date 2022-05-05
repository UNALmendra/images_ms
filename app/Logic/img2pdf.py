from fpdf import FPDF
import os

pdf = FPDF()

# path_pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
# path_img2pdf = path_pictures + "\\img2pdf\\"

path_img2pdf = 'images_ms/UNpdf/img2pdf/'

image = "images_ms/test.jpg"

def img2pdf():
    if not os.path.exists(path_img2pdf):
        os.makedirs(path_img2pdf)

    pdf.add_page()
    pdf.image(image)

    pdf.output(path_img2pdf+'output.pdf', 'F')

    return path_img2pdf