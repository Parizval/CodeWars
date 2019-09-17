# Coded by Parizval
def numericals(s):
    if len(s) == 0 : return ""
    else : 
        val = {}; ans = ""
        for i in range(len(s)):
            if s[i] not in val.keys():
                val[s[i]] = 1
                ans += "1"
            else :  
                val[s[i]] += 1 
                ans += str(val[s[i]])
        return ans
print(numericals("Hello, World!"))