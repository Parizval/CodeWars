# Circularly Sorted Array

## Description

Write a method, isCircleSorted(int[] A) ( Java, JavaScript, PHP, Haskell ) or Array#circularly_sorted? ( Ruby ), that determines if A is circularly sorted. An Array is circularly sorted if the elements are sorted in ascending order, but displaced, or rotated, by any number of steps.

## TestCases

    True
    isCircleSorted([2,3,4,5,0,1]);
    isCircleSorted([4,5,6,9,1]);
    isCircleSorted([10,11,6,7,9]);
    isCircleSorted([1,2,3,4,5]);
    isCircleSorted([5,7,43,987,-9,0]);
    
    False
    
    isCircleSorted([4,1,2,5]);
    isCircleSorted([8,7,6,5,4,3]);
    isCircleSorted([6,7,4,8]);
    isCircleSorted([7,6,5,4,3,2,1]);