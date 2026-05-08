# 6. Write a program in python to implement Queue data structure using array.
class ArrayQueue:
  def __init__(self, capacity=5):
    self.capacity = capacity
    self.queue = []

  def enqueue(self, item):
    if len(self.queue) == self.capacity:
      print("Queue is full")
    else:
      self.queue.append(item)

  def dequeue(self):
    if len(self.queue) == 0:
      print("Queue is empty")
      return None
    else:
      return self.queue.pop(0)

  def front_element(self):
    if len(self.queue) == 0:
      return None
    return self.queue[0]

  def size(self):
    return len(self.queue)

  def is_empty(self):
    return len(self.queue) == 0


if __name__ == "__main__":
  q = ArrayQueue(5)
  
  q.enqueue(15)
  q.enqueue(22)
  
  print("Enqueued 15,22")
  print("Dequeued:", q.dequeue())
  print("Front element:", q.front_element())
  print("Queue size:", q.size())
