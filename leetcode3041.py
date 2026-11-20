from typing import List
nums=list(map(int,input().split()))

def maxSelectedElements(nums:List[int])->int:
    nums.sort()
    dp={}
    for x in nums:
        dp[x+1]=dp.get(x,0)+1
        dp[x]=dp.get(x-1,0)+1

    return max(dp.values()) if dp else 0

print(maxSelectedElements(nums))