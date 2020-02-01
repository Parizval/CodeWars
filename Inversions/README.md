# Calculate number of inversions in array

## Description 
    
   Array inversion indicates how far the array is from being sorted.
   
   Inversions are pairs of elements in array, that are out of order.

## Test cases

    countInversions([1,2,3,4]) // 0 inversions
    
    countInversions([1,3,2,4]) // 1 inversion: 2 and 3
    
    countInversions([4,1,2,3]) // 3 inversions: 4 and 1, 4 and 2, 4 and 3
    
    countInversions([4,3,2,1]) // 6 inversions: 4 and 3, 4 and 2, 4 and 1, 3 and 2, 3 and 1, 2 and 1
    
## Goal

The goal is to come up with a function that can calculate inversions
for any arbitary array.