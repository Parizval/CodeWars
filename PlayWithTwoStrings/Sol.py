from collections import Counter
def work_on_strings(a,b):
    freq_a = Counter(a.lower())
    freq_b = Counter(b.lower())
    ans  = ""
    for  i in a  :  
        if i.lower() in freq_b: 
            if freq_b[i.lower()] % 2 == 0 : ans += i 
            else:  ans += i.swapcase()
        else:  
            ans += i  
    for  i in b  :  
        if i.lower() in freq_a: 
            if freq_a[i.lower()] % 2 == 0 : ans += i 
            else:  ans += i.swapcase()
        else:  
            ans += i  
    return ans