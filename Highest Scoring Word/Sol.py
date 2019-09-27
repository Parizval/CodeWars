# Coded by Parzival
def high(x):
    words = x.split(" ")
    word = "" ; count = 0 ;val = 0 ;  
    for i in words:
        val = 0 
        for j in i : 
            val += ord(j) - 96
        if val > count : 
            count = val ; word = i 
    return word 
