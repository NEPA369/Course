#7. Write a program in python to implement Priority Queue data structure using array.
class Node:
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, info, priority):
        # Validate inputs
        if not info:
            raise ValueError("Info cannot be empty")
        if not isinstance(priority, int) or priority < 0:
            raise ValueError("Priority must be a non-negative integer")
        
        node = Node(info, priority)
        
        # If queue is empty, add the node
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            # Find correct position based on priority (lower priority value = higher urgency)
            inserted = False
            for i in range(len(self.queue)):
                if node.priority < self.queue[i].priority:
                    self.queue.insert(i, node)
                    inserted = True
                    break
            
            # If not inserted, add to end
            if not inserted:
                self.queue.append(node)

    def delete(self):
        # Remove and return highest priority element (front of queue)
        if len(self.queue) == 0:
            raise Exception("Queue Underflow: Cannot delete from empty queue")
        return self.queue.pop(0)

    def peek(self):
        # View highest priority element without removing
        if len(self.queue) == 0:
            raise Exception("Queue Underflow: Queue is empty")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for i, node in enumerate(self.queue):
            print(f"{i+1}. Info: {node.info}, Priority: {node.priority}")

if __name__ == "__main__":
    pq = PriorityQueue()
    
    pq.insert("Task A", 3)
    pq.insert("Task B", 1)
    pq.insert("Task C", 2)
    
    print("Priority Queue (Lower priority number = Higher urgency):")
    pq.display()
    
    print("\nDeleting highest priority task...")
    deleted = pq.delete()
    print(f"Deleted: {deleted.info} (Priority: {deleted.priority})")
    
    print("\nQueue after deletion:")
    pq.display()
    
    print(f"\nNext task to process: {pq.peek().info}")
    
    print("\nProcessing remaining tasks in order:")
    while not pq.is_empty():
        task = pq.delete()
        print(f"Processing: {task.info}")
    
    print(f"\nQueue size: {pq.get_size()}")
    print("All tasks completed!")