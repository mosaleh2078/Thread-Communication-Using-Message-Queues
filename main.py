import time
import random
from queue import PriorityQueue
from threading import Thread, current_thread

class Worker(Thread):
    def __init__(self, queue: PriorityQueue, _id: int):
        super().__init__(name=str(_id))
        self.queue = queue

    def run(self) -> None:
        while not self.queue.empty():
            item = self.queue.get()
            print(f"Thread {current_thread().name}: processing item {item[1]} with priority {item[0]}")
            time.sleep(1)

def main(thread_num: int):
    q = PriorityQueue()
    for i in range(100):
        q.put((random.randint(0, 5), random.randint(1, 100)))

    threads: list = []
    for i in range(thread_num):
        thread = Worker(q, i+1)
        thread.start()
        threads.append(thread)
    else:
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    THREAD_NUM:int = 10
    main(THREAD_NUM)