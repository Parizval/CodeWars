# Coded by Parzival
def find_x(n):
    x = 0
    val = 2*n - 1 
    a = (n-1)*n // 2 
    x += a*(val+1) + ((val*(val + 1 )) // 2 )*n
    return x