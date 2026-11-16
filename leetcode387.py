from collections import Counter 
s=input()

def firstUniqChar(s:str)->int:
    cnt=Counter(s)
    for i,c in enumerate(s):
        if cnt[c]==1:
            return i

    return False

print(firstUniqChar(s))