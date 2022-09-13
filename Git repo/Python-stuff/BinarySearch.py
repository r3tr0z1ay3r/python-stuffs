def binsearch(list:list,s):
    u = len(list)
    l = 0
    c = 0
    while (l <= u):
        mid = (l+u) // 2
        if list[mid] == s:
            c = 1
            break
        elif list[mid] > s:
            u = mid - 1
        else:
            l = mid + 1
    if c == 1:
        print("Term found at index {}".format(list.index(s)))
    else:
        print("Not found")

l = [1,2,3,4,5,6]
binsearch(l,4)