s=input()

def checkString(s:str)->bool:
    last_a=-1
    first_b=len(s)
    for i in range(len(s)):
        if s[i]=='a':
            last_a=i
        elif s[i]=='b' and first_b==len(s):
            first_b=i

    return last_a<first_b


print(checkString(s))