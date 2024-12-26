nums = [-1,0,1,2,-1,-4]
hashmap ={}
lst = []
for i in range(len(nums)):
    temparr = nums[:i] + nums[i+1:]
    hashmap ={}
    target = -nums[i]
    for j in range(len(temparr)):
        remaining = target - temparr[j]
        if remaining in hashmap:
            lst.append([nums[i], temparr[j], remaining])
        hashmap[nums[j]] = j
print(lst)