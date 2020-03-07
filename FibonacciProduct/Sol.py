def productFib(prod):
    x = 0 ; y = 1 ; temp = 0  
    ans = []
    while True:
        if x*y == prod:
            ans.append(x)
            ans.append(y)
            ans.append(True)
            break 
        elif x*y > prod: 
            ans.append(x)
            ans.append(y)
            ans.append(False)
            break 
        temp = x + y 
        x = y 
        y = temp  
    return ans

def EfficientProductFib(prod):
    x = 0 ; y = 1 ; temp = 0  
    while x*y < prod:
        x,y = y,x+y  
    return [x,y,prod == x*y]