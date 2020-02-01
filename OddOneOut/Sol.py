import collections
def odd_one_out(s):
    frequency = collections.Counter(s)
    check = {} ; ans  = []
    for  i in range(len(s)):
        if frequency[s[i]] % 2 != 0 and  s[i] not in check:
            if s.find(s[i],i+1,len(s)) == -1:
                check[s[i]] = True
                ans.append(s[i])
    #print(ans)
    return ans  