def thirt(n):
    nums = [1,10,9,12,3,4]
    number = n 
    while True:
        digit = [int(i) for i in str(number)] 
        
        temp = 0 ; start = 0 
        for i in range(len(digit)-1,-1,-1):
            temp += digit[i]*nums[start]
            start += 1 
            if start == 6 : start = 0
        
        if  temp == number : 
            return number
        else: number = temp 