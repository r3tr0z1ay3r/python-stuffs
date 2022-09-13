from function import handle_value_error
# !!! WIN CHECK IS NOT WORKING 
def draw_board():
    board1 = [" ","|"," ","|"," ","|"]
    board2 = [" ","|"," ","|"," ","|"]
    board3 = [" ","|"," ","|"," ","|"]
    return(board1,board2,board3)
def disp_board(a,b,c):
    print(*a)
    print(*b)
    print(*c)    


def player_check():
    choice = input("Does X goes to player 1 or player 2 (1/2): ")
    if handle_value_error(choice):
        choice = handle_value_error(choice)
    if choice == 1:
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"
    return(player1,player2)

def win_check(row1,row2,row3):
    row1_elms = []
    row2_elms = []
    row3_elms = []
    col_no = 0
    x_count_r1=0
    x_count_r2=0
    x_count_r3=0
    o_count_r1=0
    o_count_r2=0
    o_count_r3=0
    
    for i in row1:
        if i == "|" or i == " ":
            continue
        else:
            row1_elms.append(i)
    for i in row2:
        if i == "|" or i == " ":
            continue
        else:
            row2_elms.append(i)
    for i in row3:
        if i == "|" or i == " ":
            continue
        else:
            row3_elms.append(i)
    print(row1_elms,row2_elms,row3_elms)
    if len(row1_elms) == 0 or len(row2_elms) == 0 or len(row3_elms) == 0:
        return None
    print(len(row1_elms),len(row2_elms),len(row3_elms))
    
    
    #Checking if all the elms in a single row are same and returning win case( 1 --> O won, 0--> X won)
    if len(row1_elms) == 3:
        print("In row1")
        if len(set(row1_elms)) == 1:
            if set(row1_elms) == "X":
                return 0
            else:
                return 1
    if len(row2_elms) == 3:
        print("In row2")
        if len(set(row2_elms)) == 1:
            if set(row2_elms) == "X":
                return 0
            else:
                return 1
    if len(row3_elms) == 3:
        print("In row3")    
        if len(set(row3_elms)) == 1:
            if set(row3_elms) == "X":
                return 0
            else:
                return 1
    
    if  x_count_r1 == 3 or x_count_r2 == 3 or x_count_r3 == 3:
        return(0)
    if o_count_r1 == 3 or o_count_r1 == 3 or o_count_r1 == 3:
        return(1)
    
    #Colms check
    
    print("In col check")
    while col_no > 3:
        win_elm = ""
        if row1_elms[col_no] == row2_elms[col_no] == row3_elms[col_no]:
            win_elm = row1_elms[col_no]
            if win_elm == "X":
                return(0)
            else:
                return(1)
        else:
            pass
        col_no += 1
        
    #Diagonal check
    try:
        print("In diag check")
        if row1_elms[0] == row2_elms[1] == row3_elms[2]:
            if win_elm == "X":
                return(0)
            else:
                return(1)
        if row1_elms[2] == row2_elms[1] == row3_elms[0]:
            if win_elm == "X":
                return(0)
            else:
                return(1)
    except:
        pass
#Enter the value into the board 
#Player1 and player2 are player markers such as X and O
def main_play(player1,player2):
    print("Use the numpad as a board and enter X and 0 accordingly!")
    row1,row2,row3 = draw_board()
    isRunning = True   
    count = 2
    while isRunning:
        player1_turn = False
        player2_turn = False
        win_elm = win_check(row1,row2,row3)
        disp_board(row1,row2,row3)
        if win_elm == 0:
            print("X has won!")
            return None
        if win_elm == 1:
            print("O has won!")
            return None
        if win_elm == None:
            pass
        
        choice  = input("Use numpad as reference and enter your choice: ")
        if handle_value_error(choice):
                choice = handle_value_error(choice)
        #To find if player1's turn or player2's turn:
        if count%2 == 0:
            player1_turn = True
            player2_turn = False
        else:
            player1_turn = False
            player2_turn = True
        count += 1      
        #Player One possibilites.9
        if player1_turn == True:
            if choice == 7:
                if row1[0] == "X" or row1[0] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row1[0] = player1
            if choice == 8:
                if row1[2]  == "X" or row1[2] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row1[2] = player1
            if choice == 9:
                if row1[4] == "X" or row1[4] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row1[4] = player1
            if choice == 4:
                if row2[0] == "X" or row2[0] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row2[0] = player1
            if choice == 5:
                if row2[2] == "X" or row2[2] =="O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row2[2] = player1
            if choice == 6:
                if row2[4] == "X" or row2[4] ==  "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row2[4] = player1
            if choice == 1:
                if row3[0] == "X" or row3[0] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row3[0] = player1
            if choice == 2:
                if row3[2] == "X" or row3[2] ==  "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row3[2] = player1
            if choice == 3:
                if row3[4] == "X" or row3[4] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row3[4] = player1
                
        #Player2 possibilites
        if player2_turn == True:
            if choice == 7:
                if row1[0] == "X" or row1[0] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row1[0] = player2
            if choice == 8:
                if row1[2]  == "X" or row1[2] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row1[2] = player2
            if choice == 9:
                if row1[4] == "X" or row1[4] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row1[4] = player2
            if choice == 4:
                if row2[0] == "X" or row2[0] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row2[0] = player2
            if choice == 5:
                if row2[2] == "X" or row2[2] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row2[2] = player2
            if choice == 6:
                if row2[4] == "X" or row2[4] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row2[4] = player2
            if choice == 1:
                if row3[0] == "X" or row3[0] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row3[0] = player2
            if choice == 2:
                if row3[2] == "X" or row3[2] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row3[2] = player2
            if choice == 3:
                if row3[4] == "X" or row3[4] == "O":
                    print("There is already a marker there, Please choose a different location or position!")
                    continue
                row3[4] = player2
player1,player2 = player_check()
main_play(player1,player2)