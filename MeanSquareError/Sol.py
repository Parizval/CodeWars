def solution(array_a, array_b):
    ans = 0  
    for i in range(len(array_a)):
        diff = abs(array_a[i] - array_b[i])
        ans  += diff** 2  
    return ans / len(array_a)