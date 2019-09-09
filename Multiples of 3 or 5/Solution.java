public class Solution {

  // Coded by Parzival
  public int solution(int number) {
    number += - 1 ; 
      int a = number / 3 ; 
      int b = number / 5 ; 
      int c = number / 15 ; 
      int ans = 0 ; 
      ans += (a*( 6 + (a-1)*3))/2 ;  
      ans += (b*( 10 + (b-1)*5)) / 2 ; 
      ans -= (c*(30 + (c-1)*15)) / 2 ; 
      return ans ;  
  }
}