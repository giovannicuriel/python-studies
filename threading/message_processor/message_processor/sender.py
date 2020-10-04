import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='registrations',
  exchange_type='fanout')

channel.basic_publish(exchange='registrations',
  routing_key='',
  body='Hello world')
print(' [x] Sent Hello world')

connection.close()

