from typing import List
nums = [1,2,3,1]
k = 3

def containsNearbyDuplicate(nums: List[int], k:int)->int:
    seen={}
    for i,num in enumerate(nums):
        if num in seen and i-seen[num]<=k:
            return True
        seen[num]=i

    return False

print(containsNearbyDuplicate(nums,k))