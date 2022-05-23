from fpdf import FPDF
import os, base64



# path_pictures = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
# path_img2pdf = path_pictures + "\\img2pdf\\"

path_img2pdf = 'images_ms/UNpdf/img2pdf/'


def img2pdf(url: str):

    pdf = FPDF()

    image = url

    if not os.path.exists(path_img2pdf):
        os.makedirs(path_img2pdf)

    pdf.add_page()
    pdf.image(image, w = 200, h=150)

    pdf.output(path_img2pdf+'output.pdf', 'F')

    with open(path_img2pdf+'output.pdf', 'rb') as pdf_file:
        encodeFile = str(base64.b64encode(pdf_file.read()))
        encodeFile = encodeFile[2:-1]
        return encodeFile