from collections import namedtuple
from time import monotonic as time
import requests
import pika
from registration_processor.services import build_legacy_service
from registration_processor.utils import build_message_receiver, TaskExecutor, Task
from registration_processor.processor import build_registration_processor

task_executor = TaskExecutor()
services = build_legacy_service(requests)('http://localhost:3000/registration')
receiver = build_message_receiver(pika)('localhost', 'user-registrations', 'fanout')
__registration_processor = build_registration_processor(services, task_executor)()
receiver.register_callback(lambda message: __registration_processor.process_message(message))
