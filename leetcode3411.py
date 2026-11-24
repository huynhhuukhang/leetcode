from typing import List
import math
nums=list(map(int,input().split()))

def maxlength(nums:List[int])->int:
    n=len(nums)
    ans=1
    for i in range(n):
        curr_prod=1
        curr_gcd=0
        curr_lcm=1
        for j in range(i,n):
            x=nums[j]
            curr_prod*=x
            curr_gcd=math.gcd(curr_gcd,x)
            curr_lcm=math.lcm(curr_lcm,x)

            if curr_prod==curr_lcm*curr_gcd:
                ans=max(ans, j-i+1)
            elif curr_prod>curr_lcm*curr_gcd:
                break

    return ans

print(maxlength(nums))