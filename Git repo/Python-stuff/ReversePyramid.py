n = int(input("Enter the limit for the pattern: "))
for i in range(n):
    for j in range(n,i):
        print("*",end=" ")
    print()