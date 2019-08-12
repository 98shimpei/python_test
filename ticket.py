import my_queue
import time
import random

def simulate_line(till_show, max_time):
    pq = my_queue.Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue("person" + str(i))

    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
    return tix_sold

sold = simulate_line(5, 1)
print(sold)
