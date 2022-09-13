def angle_check(hyp,b,h):
    lhs = hyp ** 2
    rhs = b**2 + h**2
    if lhs == rhs:
        print("It is a right angle traingle")
    else:
        print("It is not a right angle triangle")
#angle_check(5,4,3)

def angle_check2(a,b,c):
    x = (a**2) + (b**2)
    y = (b**2) + (c**2)
    z = (a**2) + (c**2)
    if c**2 == x:
        print("It is a right angled triangle")
    elif b**2 == z:
        print("It is a right angled triangle")
    elif  a**2 == y:
        print("It is a right angled triangle")
    else:
        print("It is not a right angled triangle")

angle_check2(3,4,5)