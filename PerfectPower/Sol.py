def isPP(n):
    check = False
    for i in range(2,n):
        temp = i 
        count = 1 
        while temp < n : 
            temp *= i
            count += 1 
        if temp == n:
            return [i,count]
    return None