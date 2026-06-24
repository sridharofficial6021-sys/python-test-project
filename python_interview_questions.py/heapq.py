

nums=[3,2,1,5,6,4]
nums.sort(reverse=True)
print(nums[1])

import heapq
nums=[3, 2, 1, 5, 6, 4]
k=2
print(heapq.largest(k,nums[-1]))