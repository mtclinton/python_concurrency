# basic generator

def coundown(n):

    while n > 0:
        yield n
        n -= 1

c = coundown(5)

for i in c:
    print(i)

# to unblock generator call next

from collections import deque

tasks = deque()

tasks.extend([coundown(10), coundown(5), coundown(20)])

# roundrobin
def run():
    while tasks:
        task = tasks.popleft()

        try:

            x = next(task)
            print(x)
            tasks.append(task)
        except StopIteration:
            print("Task done")

run()