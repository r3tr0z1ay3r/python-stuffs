a = int(input("Enter the x^2 co-efficent: "))
b = int(input("Enter the x co-efficient: "))
c = int(input("Enter the costant value: "))
# (-b + (b^2 - 4ac)^0.5)/2a
d = b**2 - 4*a*c
d = b**2 - 4*a*c

if d == 0:
    print("roots are equal")
elif d < 0:
    print("Roots are imaginary")
    sol1 = sol2 = -b/2*a
else:
    print("Roots are real")
    sol1 = -b + d**0.5//2*a
    sol2 = -b - d**0.5//2*a

print(sol1,sol2)