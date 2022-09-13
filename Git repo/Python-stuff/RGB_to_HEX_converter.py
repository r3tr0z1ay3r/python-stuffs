

def div_rem(a):
    dividend = a // 16
    remainder = a % 16
    return(dividend,remainder)

def rgb(r,g,b):
    dict = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    hex = []
    for i in range(0,3):
        if i == 0:
            dividend,remainder = div_rem(r)
        if i == 1:
            dividend,remainder = div_rem(g)
        if i == 2:
            dividend,remainder = div_rem(b)
        if dividend  in dict.keys():
            hex.append(dict.get(dividend))
        else:
            hex.append(dividend)
            
        if remainder  in dict.keys():
            hex.append(dict.get(remainder))
        else:
            hex.append(remainder)
    hex_value = ""
    for i in hex:
        hex_value += str(i)
    return hex_value
print(rgb(0,0,0))