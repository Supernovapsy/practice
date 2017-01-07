import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    private static void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }

        int swap_total = 0;

        outerloop:
        for (int i = 0; i != n; ++i) {
            int swaps = 0;
            for (int j = n - 1; j != 0; --j) {
                if (a[j - 1] > a[j]) {
                    swap(a, j, j - 1);
                    ++swaps;
                }
            }
            if (swaps == 0) {
                break outerloop;
            }
            swap_total += swaps;
        }

        System.out.println("Array is sorted in "+swap_total+" swaps.\nFirst Element: "+a[0]+"\nLast Element: "+a[n-1]);
    }
}
