import heapq, itertools

pq = []
heapq.heappush(pq, (15, "task1"))
heapq.heappush(pq, (15, "task1"))
# heapq.heappush(pq, (15, "task2"))
# heapq.heappush(pq, (15, "task8"))
# heapq.heappush(pq, (15, "task6"))

while pq:
    priority, task = heapq.heappop(pq)
    # print(priority, task)

# counter as tie breaker --> return elements in the order they were added
counter = itertools.count()
pq = []
heapq.heappush(pq, (15, next(counter), "task1"))
heapq.heappush(pq, (15, next(counter), "task93"))
heapq.heappush(pq, (15, next(counter), "task2"))
heapq.heappush(pq, (15, next(counter), "task8"))
heapq.heappush(pq, (15, next(counter), "task6"))

while pq:
    priority, counter, task = heapq.heappop(pq)
    # print(priority, counter, task)

class SearchNode:
    def __init__(self, label, cost):
        self.label = label
        self.cost = cost
        
    def __lt__(self, other):
        if self.label == other.label:
            return self.cost > other.cost
    
    def __eq__(self, other: object) -> bool:
        return self.label  == other.label and self.cost == other.cost

class CostAndNode:
    def __init__(self, cost, node):
        self.cost = cost
        self.node = node

    # do not compare nodes
    def __lt__(self, other):
        return self.cost < other.cost

h = []
heapq.heappush(h, (1, SearchNode("Aje", "32")))
heapq.heappush(h, (1, SearchNode("Aje", "42")))
heapq.heappush(h, (1, SearchNode("Aje", "31")))
while h:
    print(heapq.heappop(h)[1].cost)



# # heappush(pq, 10)
# # heapq.heappush(pq, 5)
# # heapq.heappush(pq, 15)
# # heapq.heappush(pq, 1)

# [print(heapq.heappop(pq)) for i in range(len(pq))]



# Max heap
# heapq._heapify_max(pq) #don't do this
#The easiest way is to invert the value of the keys and use heapq. For example, turn 1000.0 into -1000.0 and 5.0 into -5.0. --> Max heap

class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

class MaxHeapObjLen(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return len(self.val) > len(other.val)
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)


maxh = []
heapq.heappush(maxh, MaxHeapObjLen("Tunde"))
heapq.heappush(maxh, MaxHeapObjLen("Adeeeeeeee"))

x = maxh[0].val  # fetch max value
x = heapq.heappop(maxh).val  # pop max value
