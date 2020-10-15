from time import sleep
import threading
import registration_processor as default_processor


def start_consumer(processor):
  processor.receiver.start()

def start_task_executor(processor):
  processor.task_executor.run()

receiver_thr = threading.Thread(target=start_consumer, args=(default_processor,))
task_thr = threading.Thread(target=start_task_executor, args=(default_processor,))

receiver_thr.start()
sleep(10)
task_thr.start()
task_thr.join()
