import my_stack
import my_queue

stack = my_stack.Stack()
queue = my_queue.Queue()
for c in "Hello":
    stack.push(c)
    queue.enqueue(c)
reverse = ""
not_reverse = ""

while not stack.is_empty():
    reverse += stack.pop()

while not queue.is_empty():
    not_reverse += queue.dequeue()

print(reverse)
print(not_reverse)
