import queue
import threading
import time

task_queue = queue.PriorityQueue()

def worker():
    while True:
        priority, task = task_queue.get()
        print(f"🔧 Processing {task} with priority {priority}")
        time.sleep(2)
        task_queue.task_done()

threading.Thread(target=worker, daemon=True).start()

# Lower number = higher priority
task_queue.put((2, "Backup"))
task_queue.put((1, "Urgent Email"))
task_queue.put((3, "Cleanup"))

task_queue.join()
