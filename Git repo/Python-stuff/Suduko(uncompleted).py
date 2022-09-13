import random as r

def  boxCount():
    box_no = r.randint(3,6)
    return box_no
def to_fill(count):
    nums_to_fill = []
    #To get the correct amount of elemnts while avoiding repeated elemns
    while len(nums_to_fill) != count:
        current = r.randint(1,9)
        if current in nums_to_fill:
            continue
        nums_to_fill.append(current)
    return list(nums_to_fill)

def square():
    row = r.randint(0,2)
    column = r.randint(0,2)
    return [row],[column]



#One square format 
square1 = [["","",""],["","",''],['','','']]
square2 = square1.copy()
square3 = square1.copy()

def genSquare(square1):
    #Getting a randomised no of items to fill and where to fill
    count = boxCount()
    nums = to_fill(count)

    #Using the randomised values to fill up symbolizing a suduko square
    for i in nums:
        row,col = square()
        row,col = row[0],col[0]
        square_row = square1[row]
        square_row[col] = i
    return square1
print(genSquare(square1))
print(genSquare(square2))
print(genSquare(square3))

