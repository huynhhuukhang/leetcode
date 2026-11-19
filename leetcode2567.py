from typing import List
nums=list(map(int,input().split()))

def minimizeSum(nums:List[int])->int:
    nums.sort()
    return min(nums[-1]-nums[2], nums[-3]-nums[0], nums[-2]-nums[1])

print(minimizeSum(nums))