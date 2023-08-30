class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.pop(0)

  def is_empty(self):
    return self.queue == []

  def size(self):
    return len(self.queue)


def cafe(log):
  queue = Queue()
  barista_1_time = barista_2_time = 0
  max_time = 0
  customer_wait = 0
  current_index = 0
  customer_list = []

  for item in log:
    queue.enqueue([int(item[0]), int(item[1])])

  while not queue.is_empty():
    current_index += 1
    current_customer = queue.dequeue()
    if barista_1_time >= barista_2_time and current_customer[0] <= barista_1_time:
      barista_1_time, barista_2_time = barista_2_time, barista_1_time
    if current_customer[0] > barista_1_time:
      barista_1_time = current_customer[0]

    if max_time < barista_1_time - current_customer[0]:
      max_time = barista_1_time - current_customer[0]
      customer_wait = current_index
    barista_1_time += current_customer[1]

    customer_list.append([barista_1_time, current_index])

  customer_list.sort()

  for customer in customer_list:
    print(f'Time {customer[0]} customer {customer[1]} get coffee')

  if customer_wait == 0 and max_time == 0:
    print('No waiting')
  else:
    print(f'''The customer who waited the longest is : {customer_wait}
The customer waited for {max_time} minutes''')


if __name__ == '__main__':
  print(" ***Cafe***")
  log = [i.split(',') for i in input('Log : ').split("/")]

  cafe(log)