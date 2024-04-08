import heapq

num = [1,2,3,4,5]

# max
num = [-r for r in num]

# min
heapq.heapify(num)

for item in num:
    print("Item in heap:",item)