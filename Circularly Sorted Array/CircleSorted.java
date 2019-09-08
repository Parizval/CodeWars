public class CircleSorted {

    // Code by Parzival
    public boolean isCircleSorted(int[] a) {
        int index = 0 ;
        int min = a[0] ;
        for (int i = 1; i < a.length; i++) {
            if(min > a[i])
            {
                min = a[i];
                index = i ;
            }
        }
        System.out.println("pos"+index);
        if(index == 0 )
        {
            for (int i = 1; i < a.length; i++) {
                if(a[i-1] > a[i])
                {
                    return false;
                }
            }
            return true;
        }
        else{
            System.out.println("esls");
            int last = a[a.length - 1 ] ;
            for (int i = index + 1; i < a.length; i++) {
                if(a[i-1] > a[i])
                {
                    return false;
                }
            }
            if(last > a[0])
            {
                return false;
            }
            for (int i = 1; i < index; i++) {
                if(a[i-1] > a[i])
                {
                    return false;
                }
            }
            return true ;
        }

   }
}