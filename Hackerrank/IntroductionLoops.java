package Hackerrank;

import java.util.Arrays;

public class IntroductionLoops {
    public static void main(String[] args) {
        int a[]={1,2,3,4};
        System.out.println(Arrays.toString(a));
        int b[] = new int[a.length];
        for(int i = 0; i < a.length; i++) {  
            b[i]=(a[i]*a[i]);
        }
        System.out.println(Arrays.toString(b));
        
    }
}
