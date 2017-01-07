import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static long makeChange(int[] coins, int money) {
        // This is a DP problem.
        /*
        Make array of Hashsets of lists of size coins.size storing the subproblem solutions, consisting of the
        list of coin combinations summing to the money sum for that index=money.

        At each round, congregate the lists together without duplicates.
        HashSet is used to prevent any duplicates from appearing in the set.
        */

        int solution_len = money + 1;

        List<HashSet<ArrayList<Integer>>> dp =
                new ArrayList<HashSet<ArrayList<Integer>>>(solution_len);

        ArrayList<Integer> emptyList = new ArrayList<Integer>(coins.length);
        for (int i = 0; i != coins.length; ++i) {
            emptyList.add(0);
        }
        dp.add(new HashSet<ArrayList<Integer>>());
        dp.get(0).add(emptyList);
        assert dp.get(0).size() == 1;

        for (int i = 1; i != solution_len; ++i) {
            HashSet<ArrayList<Integer>> newSet = new HashSet<ArrayList<Integer>>();
            for (int j = 0; j != coins.length; ++j) {
                int coin = coins[j];
                if (coin <= i) {
                    for (ArrayList<Integer> list : dp.get(i - coin)) {
                        ArrayList<Integer> newList = (ArrayList<Integer>)list.clone();
                        newList.set(j, newList.get(j) + 1);
                        newSet.add(newList);
                    }
                }
            }
            dp.add(newSet);
        }

        return dp.get(money).size();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int coins[] = new int[m];
        for(int coins_i=0; coins_i < m; coins_i++){
            coins[coins_i] = in.nextInt();
        }
        System.out.println(makeChange(coins, n));
    }
}
