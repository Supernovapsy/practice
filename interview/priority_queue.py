import heapq
import itertools

counter = itertools.count()
pq = []
task_map = {}
REMOVED = '<removed-task>'

def push(task, priority=0):
    if task in task_map:
        remove(task)
    entry = [priority, next(counter), task]
    task_map[task] = entry
    heapq.heappush(pq, entry)

def remove(task):
    entry = task_map[task]
    entry[-1] = REMOVED

def pop():
    while pq:
        task = heapq.heappop(pq)[-1]
        del task_map[task]
        if task != REMOVED:
            return task
    raise KeyError("Pop from empty heap!")

if __name__ == "__main__":
    push("how", 3)
    push("are", 30)
    push('hello', 2)
    push("you?", 100)

    print pop()
    print pop()
    print pop()
    print pop()
    print pop()
