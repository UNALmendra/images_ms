## UNpdf

## images_ms

Microservicio para convertir imagenes en pdf y viceversa.

## Docker install

```shell
docker build -t images_ms .
docker run -it --name images_ms -p 5000:3000 -v "$(PWD)\UNpdf:/images_ms/UNpdf/" images_ms