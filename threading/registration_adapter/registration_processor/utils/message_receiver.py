"""RabbitMQ consumer"""
import json


def build_message_receiver(pika):
    """Build a RabbigMQ message receiver

    It is expected to use `pika` as interface access to RabbitMQ broker
    """
    class Receiver:
        """Message receiver class

        This class will use RabbitMQ to receive messages. Both exchange name and
        type are configurable.
        """

        def __init__(self, host, exchange, exchange_type):
            self.__connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=host
            ))
            self.__channel = self.__connection.channel()
            self.__channel.exchange_declare(
                exchange=exchange, exchange_type=exchange_type)
            self.__queue_name = self.__channel.queue_declare(
                '', exclusive=True).method.queue
            self.__channel.queue_bind(exchange=exchange,
                                      queue=self.__queue_name)

        def __build_callback_wrapper(self, callback_fn):
            def wrapper(_channel, method, _properties, body):
                callback_fn(json.loads(body))
                self.__channel.basic_ack(delivery_tag=method.delivery_tag)
            return wrapper

        def register_callback(self, callback_fn):
            """Register callback function for message processing

            This callback function will have only one parameter, which will be the
            message body. Its return value will be ignored. Please, do not
            throw any exceptions, it will break everything.

            #todo: deal with exceptions.

            :param function callback_fn: The single-parameter callback function.
            """
            callback = self.__build_callback_wrapper(callback_fn)
            self.__channel.basic_consume(
                queue=self.__queue_name, on_message_callback=callback)

        def start(self):
            """Start message consumption

            This is a blocking function. It should be a thread. WHICH IS THE
            PURPOSE OF THIS WHOLE THING. Are you getting it?
            """
            self.__channel.start_consuming()
    return Receiver
