def IsAnagram(w1,w2):
    anagram = True
    if w1 == w2:
        return True
    for letter in w2:
        if letter  in w1:
            pass
        if anagram == True and w1.count(letter) == w2.count(letter):
            anagram = True
        else:
            anagram = False
    return  anagram

def anagrams(word, words):
    w1 = word
    out = []
    for i in words:
        if IsAnagram(w1,i):
            out.append(i)
    return out

