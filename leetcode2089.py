from typing import List
target=int(input())
nums=list(map(int,input().split()))

def targetIndices(nums:List[int], target:int)->List[int]:
    less=0
    equal=0
    for num in nums:
        if num< target:
            less+=1
        if num==target:
            equal+=1

    return list(range(less,less+equal))

print(targetIndices(nums,target))