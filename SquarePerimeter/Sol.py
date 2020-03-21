def perimeter(n):
    ans = 8 ;a = 1; b = 1 
    for i in range(n-1):
        a,b = a+b,a
        ans += 4*a
    return ans