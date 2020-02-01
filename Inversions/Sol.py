def count_inversions(array):
    check = True
    ans  = 0 
    while check:
        check = False
        for i in range(len(array)-1):
            if array[i] >  array[i+1]:
                ans  += 1 
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp 
                check = True
    return ans