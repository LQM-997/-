def fun(s):
    if(len(s)==0 or len(s)==1):
        return s
    else:
        return fun(s[1:])+s[0]
s="abcde"
print(fun(s))
        
