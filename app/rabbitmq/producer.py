import json
import pika

credentials = pika.PlainCredentials('unpdf', 'unpdf')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 8888, credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='Logs')

example_msg = {
    'doc': '100',
    'user': 'Juan',
    'description': 'Convertido de pdf a imagen',
}

channel.basic_publish(  exchange='',
                        routing_key='Logs',
                        body=json.dumps(example_msg)) #BODY ES EL MESANJE A ENVIAR DESPUES DE RECIBIR DEL MICROSERVICIO DOCS

print("[x] Enviado Log Convertido de pdf a imagen")

connection.close()