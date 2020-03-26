from collections import Counter 
def palindrome(num):
    if type(num) == str or  num < 0  : return 'Not valid' 
    letter = Counter(str(num))
    ans = 0 ; check = False
    for k,v in letter.items(): 
        if k.isalnum():
            if v  % 2 == 1 : check = True
            ans += int(v/2)*2
    if  check: ans += 1  
    if ans == len(str(num)) and ans > 1: return True
    return False
