import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    private static int[] leftArray;
    private static int[] rightArray;

    private static long countInversionsAux(int[] arr, int i, int j) {
        if (j - i == 1) {
            return 0;
        }

        // Divide & accumulate.
        int mid = (i + j) / 2;
        long acc = countInversionsAux(arr, i, mid) + countInversionsAux(arr, mid, j);

        // Counting inversions between the left and right sections.
        int index = mid;
        for (int left = i; left != mid; ++left) {
            while (index != j && arr[index] < arr[left])
                ++index;
            acc += index - mid;
        }

        // Merge Sort.
        int leftLength = mid - i, rightLength = j - mid;
        System.arraycopy(arr, i, leftArray, 0, leftLength);
        System.arraycopy(arr, mid, rightArray, 0, rightLength);

        int left = 0, right = 0;
        index = i;
        while (left != leftLength && right != rightLength) {
            if (leftArray[left] <= rightArray[right]) {
                arr[index++] = leftArray[left++];
            } else {
                arr[index++] = rightArray[right++];
            }
        }
        System.arraycopy(leftArray, left, arr, index, leftLength - left);
        System.arraycopy(rightArray, right, arr, index, rightLength - right);

        return acc;
    }

    public static long countInversions(int[] arr){
        // idea: merge sort, and within each step count the # of inversions.
        // Add them up and accumulate.
        leftArray = new int[arr.length / 2 + 1];
        rightArray = new int[arr.length / 2 + 1];
        return countInversionsAux(arr, 0, arr.length);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int arr[] = new int[n];
            for(int arr_i=0; arr_i < n; arr_i++){
                arr[arr_i] = in.nextInt();
            }
            System.out.println(countInversions(arr));
//             for (int i = 0; i != arr.length; ++i) {
//                 System.out.println(arr[i]);
//             }
        }
    }


}
