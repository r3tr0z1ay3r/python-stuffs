a = 1652
def nar_check(a):
    a = str(a)
    len_a = len(a)
    sum = 0
    for i in a:
        sum += int(i) ** len_a 

    if sum == int(a):
        return True
    else:
        return False