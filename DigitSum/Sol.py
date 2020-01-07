def digital_root(n):
    string = str(n); total = 0 ; 
    while True:
        nums = [int(i) for i in string ] 
        total = sum(nums)
        if len(str(total)) == 1 :  
            return total
        else:
            string = str(total)