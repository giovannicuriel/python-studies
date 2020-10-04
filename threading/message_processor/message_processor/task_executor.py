from collections import namedtupe
"""
Este executor é baseado na implementação do scheduler do Python. Coloquei aqui
para fins de exemplo de uso do mutex.

https://github.com/python/cpython/blob/3.8/Lib/sched.py
"""


class Task(namedtuple('Task', ['time', 'action'])):


class TaskExecutor:
  type_table: List[TimeEntry]
  
  def __init__(self):
    self.time_table = []

  def run(self):
    while self.time_table:
      self.time_table[0].diff_time -= .1
      [ fn() for fn in self.time_table[0].fns if self.time_table[0].diff_time < 0 ]

        
  def add_task(self, timeout, fn):
    ix = 0
    for time_entry in self.time_table:
      ix += 1
      if (timeout - time_entry.diff_time) < 0:
        # Found where
        new_time_entry = TimeEntry(fn=fn, diff_time=timeout)
        self.time_table.insert(ix, new_time_entry)
        break
      else:
        timeout -= time_entry.diff_time


executor = TaskExecutor()
executor.add_task()