"""Send a message to the default exchange for this app"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='user-registrations',
  exchange_type='fanout')

channel.basic_publish(exchange='user-registrations',
  routing_key='',
  body='{"name": "John Doe", "age": 36}')
print(' [x] Sent user creation')

connection.close()
