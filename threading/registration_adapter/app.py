"""Main processor app"""
from time import sleep
import threading
from registration_processor import build_registration_processor


def start_consumer(processor):
    """Consumer thread"""
    print('Starting consumer thread')
    processor.receiver.start()


def start_task_executor(processor):
    """Task executor thread"""
    print('Starting task executor thread')
    processor.task_executor.run()

default_processor = build_registration_processor()
receiver_thr = threading.Thread(
    target=start_consumer, args=(default_processor,))
task_thr = threading.Thread(
    target=start_task_executor, args=(default_processor,))

receiver_thr.start()
sleep(10)
task_thr.start()
task_thr.join()
