# Row of the odd triangle

## Description
    
Given a triangle of consecutive odd numbers:
                
                1
              3     5
           7     9    11
       13    15    17    19
    21    23    25    27    29
    ...
    
   find the triangle's row knowing its index (the rows are 1-indexed), e.g.:
## Test Cases

    odd_row(1)  ==  [1]
    odd_row(2)  ==  [3, 5]
    odd_row(3)  ==  [7, 9, 11]