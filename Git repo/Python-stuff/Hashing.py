#Hashing with linear probing
def linear_prob(val,table):
    for i in range(len(table)):
        pos_update = ((val+i)%len(table))
        if table[pos_update] != 0:
            continue
        else:
            table[pos_update] = val
            break
def hash_table(n):
    table = []
    for i in range(n):
        table.append(0)
    return table
        
    
def hash(val,table):
    pos = val % len(table)
    if table[pos] != 0:
        linear_prob(val,table)
    else:
        table[pos] = val



table = hash_table(10)
hash(89,table)
hash(79,table)
print(table)
