## UNpdf

## images_ms

Microservicio para convertir imagenes en pdf y viceversa.

## Docker install

```shell
docker build -t images_ms .
docker run -it --name images_ms -p 3000:3000 -v "$(PWD)\UNpdf:/images_ms/UNpdf/" images_ms
```


## Routes

```shell
'localhost:3000/img2pdf' # -> Convertir de imagen a pdf
'localhost:3000/pdf2img' # -> Convertir de pdf a imagen (Todo el archivo)
'localhost:3000/img2pdf/a-b' # -> Convertir de pdf a imagen (las paginas en el rango a-b inclusive)
```
