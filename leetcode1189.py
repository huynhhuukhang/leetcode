from collections import Counter
text=input()

def maxNumberOfBalloons(text:str)->int:
    cnt=Counter(text)
    return min(cnt['b'], cnt['a'], cnt['n'], cnt['l']//2, cnt['o']//2)


print(maxNumberOfBalloons(text))