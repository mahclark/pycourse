from queue import PriorityQueue
import heapq

q = [7,6,5,4,3,2,1]
heapq.heapify(q)
heapq.heappop(q)
print(q)