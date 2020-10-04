from message_processor.task_executor import TaskExecutor, Task
from time import monotonic as time
from message_processor.receiver import Receiver


# executor = TaskExecutor()
# executor.add_task(time() + 2, lambda: print('Two seconds delay'))
# executor.add_task(time() + 5, lambda: print('Five seconds delay'))
# executor.add_task(time() + 7, lambda: print('Seven seconds delay'))
# executor.run()

receiver = Receiver()
receiver.register_callback(lambda body: print(f"[l] Received: {body}"))
receiver.start()
