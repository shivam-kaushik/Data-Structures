s = "dvdf"

lst = []
tempLen = 0
maxLen = 0

for i in range(len(s)):
    if s[i] not in lst:
        lst.append(s[i])
        tempLen+=1
    else:
        while s[i] in lst:
            lst.pop(0)
            tempLen-=1
        lst.append(s[i])
        tempLen += 1
    if tempLen>maxLen:
        maxLen = tempLen

print(maxLen)