from flask import Flask, jsonify
from flask_restful import Resource, Api

from Logic.img2pdf import img2pdf
from Logic.pdf2img import pdf2img


app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return jsonify({"message": "Holaaaaa!!"})

class ConvertPDF(Resource):
    def post(self):
        return jsonify({"message": 'Archivo convertido exitosamente. Imagen guardada en ' + pdf2img()})

class ConvertPDFRange(Resource):
    def post(self, firstPage, lastPage):
        return jsonify({"message": 'Archivo convertido exitosamente. Imagen guardada en ' + pdf2img(firstPage, lastPage)})

class ConvertImg(Resource):
    def post(self):
        return jsonify({"message": 'Archivo convertido exitosamente. pdf guardado en ' + img2pdf()})


api.add_resource(ConvertPDF, '/pdf2img')
api.add_resource(ConvertPDFRange, '/pdf2img/<int:firstPage>-<int:lastPage>')
api.add_resource(ConvertImg, '/img2pdf')

api.add_resource(Welcome, "/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)