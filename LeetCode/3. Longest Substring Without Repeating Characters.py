s = "abcabcbb"

lst =[s[0]]
tempLen = 1
maxLen = 1

for i in range(1, len(s)):
    if s[i] not in lst:
        
        lst.append(s[i])
        tempLen+=1
    else:
        tempLen = 1
    if tempLen>maxLen:
        maxLen = tempLen

print(maxLen)