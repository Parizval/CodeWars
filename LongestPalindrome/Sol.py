from collections import Counter 
def longest_palindrome(s):
    s  = s.lower()
    letter = Counter(s)
    ans = 0 ; check = False
    for k,v in letter.items(): 
        if k.isalnum():
            if v  % 2 == 1 : check = True
            ans += int(v/2)*2
    if  check: ans += 1  
    return ans