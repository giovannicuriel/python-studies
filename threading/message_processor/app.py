from message_processor.task_executor import TaskExecutor, Task
from time import monotonic as time
from message_processor.receiver import Receiver

from message_processor.processor import MessageProcessor
from message_processor.services.legacy_service import LegacyService

executor = TaskExecutor()
# executor.add_task(time() + 2, lambda: print('Two seconds delay'))
# executor.add_task(time() + 5, lambda: print('Five seconds delay'))
# executor.add_task(time() + 7, lambda: print('Seven seconds delay'))
# executor.run()

# receiver = Receiver()
# receiver.register_callback(lambda body: print(f"[l] Received: {body}"))
# receiver.start()


legacy_service = LegacyService('http://localhost:3000/registration')
processor = MessageProcessor(legacy_service, executor)
user = {
  'name': 'Giovanni',
  'age': 36
}

processor.process_message(user)

executor.run()