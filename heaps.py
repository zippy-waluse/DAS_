import heapq

# num = c

# max
# num = [-r for r in num]

# min
# heapq.heapify(num)

# for item in num:
#     print("Item in heap:",item)

    # print(num)

    # heapq.heappop(num)
    # print(heap)


# heapq.heappush(num,2)
# print(num)



import heapq
num= [1,2,3,4,5]
heapq.heapify(num)
print(num)

heapq.heappush(num,9)
print(num)

heapq.heappushpop(num,2)
print(num)



