def highest_rank(arr):
    number =  0 ; count = 0 ; 
    for i in arr:
        if count == 0 : 
            number = i ; count = arr.count(i)
        else:
            if arr.count(i) > count : 
                number = i ; count = arr.count(i)
            elif arr.count(i) == count : 
                number = max(number,i)
    return number

highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12])