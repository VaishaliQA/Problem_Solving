'''
list
collections.deque
queue.Queue
'''

class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,val):
        self.queue.append(val)
    def dequeue(self):
        if(len(self.queue)< 1):
            return None
        return self.queue.pop(0)
    def display(self):
        print("display data",self.queue)  
    def size(self):
        
        return len(self.queue)

queueData = Queue()
queueData.enqueue(10)
queueData.enqueue(20)
queueData.enqueue(30)
queueData.enqueue(40)
print("size of queue",queueData.size())
queueData.display()
queueData.dequeue()
queueData.display()
queueData.dequeue()
queueData.enqueue(50)
queueData.enqueue(60)
queueData.dequeue()
queueData.display()
print("size of queue",queueData.size())