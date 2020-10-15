from collections import namedtuple
import heapq
from time import sleep
from time import monotonic as _time

"""
Este executor é uma versão reduzida do código do scheduler do Python. Coloquei
aqui para exemplificar o uso do mutex (a ser feito ainda)

O código original é este
https://github.com/python/cpython/blob/3.8/Lib/sched.py
"""


class Task(namedtuple('Task', ['time', 'action'])):
  def __eq__(self, o): return self.time == o.time
  def __lt__(self, o): return self.time <  o.time
  def __le__(self, o): return self.time <= o.time
  def __gt__(self, o): return self.time >  o.time
  def __ge__(self, o): return self.time >= o.time

class TaskExecutor:
  _time_table = []
  
  def __init__(self):
    pass

  def run(self):
    while self._time_table:
      time, fn = self._time_table[0]
      now = _time()
      if time > now:
        print(f'Sleeping {time-now} until next run')
        sleep(time - now)
      else:
        heapq.heappop(self._time_table)
        fn()
      
        
  def add_task(self, timeout, fn):
    task = Task(_time() + timeout, fn)
    heapq.heappush(self._time_table, task)
