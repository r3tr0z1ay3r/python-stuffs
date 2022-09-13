a = [9,4,2,6,1]

for i in range(len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            min = j
    a[i],a[min] = a[min],a[i]
print(a)