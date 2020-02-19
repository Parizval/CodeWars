def infected(s):
    total = 0
    infected = 0
    check = False
    temp = 0 
    for i in s:
        if i == "0" or i =="1": 
            total += 1
            temp += 1 
            if i == "1" :  
                check = True
        else:
            if  check:
                infected += temp  
                check = False
            temp = 0
    if check: infected += temp
    if total == 0 : return total
    return (100*infected)/total