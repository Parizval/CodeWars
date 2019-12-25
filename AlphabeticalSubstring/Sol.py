def longest(s):
    string = s[0]
    substring = s[0] ; 
    for i in range(1,len(s)):
        if ord(s[i]) >= ord(s[i-1]) : 
            substring += s[i]
        else: 
            if len(substring) > len(string):
                string = substring   
                substring = ""
            else:
                substring = s[i]
    if len(substring) > len(string): return substring
    return string