from random import *
from SimpleEnglishWords import all_words

english_words = all_words()
print(len(english_words))
to_find = english_words[randint(0,len(english_words))]
print(to_find)
random_word = english_words[randint(0,len(english_words))]

to_find_ = []
for i in to_find:
    to_find_.append("_")

print(*to_find_)



count = True
num = 0
while count == True:
    word = input("Enter a alphabet to guess: ")
    for i in range(0,len(to_find)):
        if word == to_find[i]:
            to_find_[i] = word
        if "_" not in to_find_:
            print("Congratulation u have succesfully found out the word")
            count = False
        if num == 8:
            print("You are out of tries....You lose!")
            count = False
    print(f"You have {8-num} tries left")
    print(*to_find_)
    num+=1