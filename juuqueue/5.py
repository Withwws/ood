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

  def first(self):
    return self.queue[0]

  def last(self):
    return self.queue[-1]


def search_portal(width, height, room):
  queue = Queue()
  visited = []

  if len(room) != height:
    print("Invalid map input.")
    return

  for i in room:
    if len(i) != width:
      print("Invalid map input.")
      return

  for i, floor in enumerate(room):
    for j, tile in enumerate(floor):
      if tile == 'F':
        queue.enqueue((j, i))
        visited.append((j, i))

  if queue.is_empty():
    print("Invalid map input.")
    return

  while True:
    if queue.is_empty():
      print('Cannot reach the exit portal.')
      break

    print(f'Queue: {queue.queue}')

    currentX, currentY = queue.first()[0], queue.first()[1]

    if currentY > 0 and room[currentY-1][currentX] == '_' and (currentX, currentY-1) not in visited:
      queue.enqueue((currentX, currentY-1))
      visited.append((currentX, currentY-1))

    if currentX < width - 1 and room[currentY][currentX+1] == '_' and (currentX+1, currentY) not in visited:
      queue.enqueue((currentX+1, currentY))
      visited.append((currentX+1, currentY))

    if currentY < height - 1 and room[currentY+1][currentX] == '_' and (currentX, currentY+1) not in visited:
      queue.enqueue((currentX, currentY+1))
      visited.append((currentX, currentY+1))

    if currentX > 0 and room[currentY][currentX-1] == '_' and (currentX-1, currentY) not in visited:
      queue.enqueue((currentX-1, currentY))
      visited.append((currentX-1, currentY))

    if currentY > 0 and room[currentY-1][currentX] == 'O' and (currentX, currentY-1) not in visited:
      print('Found the exit portal.')
      break

    if currentX < width - 1 and room[currentY][currentX+1] == 'O' and (currentX+1, currentY) not in visited:
      print('Found the exit portal.')
      break

    if currentY < height - 1 and room[currentY+1][currentX] == 'O' and (currentX, currentY+1) not in visited:
      print('Found the exit portal.')
      break

    if currentX > 0 and room[currentY][currentX-1] == 'O' and (currentX-1, currentY) not in visited:
      print('Found the exit portal.')
      break

    queue.dequeue()


if __name__ == '__main__':
  width, height, room = input('Enter width, height, and room: ').split()

  search_portal(int(width), int(height), room.split(','))