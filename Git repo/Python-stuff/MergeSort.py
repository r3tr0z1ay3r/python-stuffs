a = [10,2,5,3,7,9,1]

#Find half point
half = len(a)//2
first = a[:half]
second = a[half:]

first_half = len(first) // 2
first2 = first[:first_half]
first3 = first[first_half:]

for i in first2:
    if len(first2)