"""Task executor module.

This is a shameless ripoff of oficial Python `sched`module. I put it here so
that it become clearer to show how threads and its associated control structures
(semaphores, mutexes, signals, and so on) are supposed to be used - I did not
add them, though.

The original module is this:
https://github.com/python/cpython/blob/3.8/Lib/sched.py
"""
from collections import namedtuple
import heapq
from time import sleep
from time import monotonic as _time


class Task(namedtuple('Task', ['time', 'action'])):
    """Task class"""

    def __eq__(self, o):
        return self.time == o.time
    def __lt__(self, o):
        return self.time < o.time
    def __le__(self, o):
        return self.time <= o.time
    def __gt__(self, o):
        return self.time > o.time
    def __ge__(self, o):
        return self.time >= o.time


class TaskExecutor:
    """Task executor

    This class is indeed very simple: add a task with a fixed time indicating
    when it should be executed. Add it in an ordered queue. For the main
    execution loop, sleep a bit until the next task should be executed. When
    the time comes, pop the task from the queue, execute it and go back to
    sleep. Just like me on holidays.
    """
    _time_table = []

    def __init__(self):
        pass

    def run(self):
        """Execution main loop

        This function is supposed to never exit (except, of course, if a "STAHP
        NOW BRO" signal is sent to its thread. In that case, it will exit as
        soon as possible. This is yet to be implemented).
        """
        while self._time_table:
            time, callback_fn = self._time_table[0]
            now = _time()
            if time > now:
                print(f'Sleeping {time-now} until next run')
                sleep(time - now)
            else:
                heapq.heappop(self._time_table)
                callback_fn()

    def add_task(self, timeout, callback_fn):
        """Add a new task to the execution queue

        :param int timeout: Number of seconds before task execution.
        :param function callback_fn: The function to be called. It should have no
        arguments
        """
        task = Task(_time() + timeout, callback_fn)
        heapq.heappush(self._time_table, task)
