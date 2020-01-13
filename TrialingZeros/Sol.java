public class Solution {
  public static int zeros(int n) {
      // your beatiful code here
      int count = 0;
      for (int i = 5; n / i >= 1; i *= 5) 
          count += n / i; 
  
        return count; 
  }
}