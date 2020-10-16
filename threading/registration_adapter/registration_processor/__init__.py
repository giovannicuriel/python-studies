"""Registration processor default structures"""

from collections import namedtuple
from time import monotonic as time
import requests
import pika
from .services import build_legacy_service
from .utils import build_message_receiver, TaskExecutor, Task
from .processor import build_processor


def build_registration_processor():
    """Build registration processor default strucutures"""
    task_executor = TaskExecutor()
    services = build_legacy_service(requests)(
        'http://localhost:3000/registration')
    receiver = build_message_receiver(pika)(
        'localhost', 'user-registrations', 'fanout')
    __registration_processor = build_processor(
        services, task_executor)()
    receiver.register_callback(__registration_processor.process_message)

    RegistrationProcessor = namedtuple('RegistrationProcessor', [
                                       'task_executor', 'receiver'])
    return RegistrationProcessor(task_executor=task_executor, receiver=receiver)
