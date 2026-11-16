from typing import List
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))

def intersection(nums1: List[int], nums2:List[int])->List[int]:
    nums1.sort()
    nums2.sort()
    res=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        else:
            if not res or res[-1]!=nums1[i]:
                res.append(nums1[i])
            i+=1
            j+=1

    return res

print(*intersection(nums1,nums2))