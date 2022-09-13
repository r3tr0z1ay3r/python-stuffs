def rom(a):
    n = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    s = ['I',"IV","V","IX",'X','XL','L',"XC","C",'CD',"D","CM","M"]
    i = 12
    output = []
    while a:
        div = a//n[i]
        a = a % n[i]
        print(div,a, )
        while div:
            output.append(s[i])
            div -=1
        i -=1
    return (output)
x = int(input("Enter a integer"))
out = rom(x)
print("The roman form of the give number will be: ",*out,sep="")
