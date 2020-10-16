import json
def build_message_receiver(pika):
  class Receiver:
    def __init__(self, host, exchange, exchange_type):
      self.__connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host
      ))
      self.__channel = self.__connection.channel()
      self.__channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)
      self.__queue_name = self.__channel.queue_declare('', exclusive=True).method.queue
      self.__channel.queue_bind(exchange=exchange,
        queue=self.__queue_name)

    def __build_callback_wrapper(self, fn):
      def wrapper(channel, method, properties, body):
        fn(json.loads(body))
        self.__channel.basic_ack(delivery_tag = method.delivery_tag)
      return wrapper

    def register_callback(self, fn):
      callback = self.__build_callback_wrapper(fn)
      self.__channel.basic_consume(queue=self.__queue_name, on_message_callback=callback)
    
    def start(self):
      self.__channel.start_consuming()
  return Receiver
