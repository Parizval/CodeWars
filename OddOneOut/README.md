# What will be the odd one out?

## Description 

Write a function that will take in a string and return all the unpaired characters (show up an odd number of times in the string) in the order they were encountered as an array. In case of multiple options to choose from, take the last occurence as the unpaired character.

#### Notes

-  A wide range of characters is used, and some of them may not render properly in your browser.
-  Your solution should be linear in terms of string length to pass the last test.

## Testcases
    
    odd_one_out('Hello World')   ==  ["H", "e", " ", "W", "r", "l", "d"]
    odd_one_out('Codewars')      ==  ["C", "o", "d", "e", "w", "a", "r", "s"]
    odd_one_out('woowee')        ==  []
    odd_one_out('wwoooowweeee')  ==  []
    odd_one_out('racecar')       ==  ["e"]
    odd_one_out('Mamma')         ==  ["M"]
    odd_one_out('Mama')          ==  ["M", "m"]