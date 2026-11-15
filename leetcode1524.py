from typing import List
arr=[1,3,5]

def numOfSubarrays(arr: list[int])->int:
    MOD=10**9+7
    even=1
    odd=0
    curr=0
    ans=0
    for num in arr:
        curr+=num
        if curr%2==1:
            ans+=even
            odd+=1
        else:
            ans+=odd
            even+=1

    return ans%MOD



print(numOfSubarrays(arr))