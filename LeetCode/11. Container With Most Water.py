height = [1,8,6,2,5,4,8,3,7]

max_area = 0
i = 0
j = len(height)-1
while i<j:
    temp = min(height[i], height[j]) * (j - i)
    max_area = max(temp, max_area)
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1
print(max_area)