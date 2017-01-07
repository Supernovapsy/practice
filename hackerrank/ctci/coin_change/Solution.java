import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    private static long[][] mem;

    private static long dp(int money, int i, int[] coins) {
        if (money == 0) {
            // This ensures that money = 0 is only counted as one way.
            return 1;
        } else if (i == coins.length) {
//             System.out.println("reached beyond last coin.");
            return 0;
        } else if (mem[money][i] != -1) {
//             System.out.println("stored (i = " + i + ", money = " + money + ", subtotal = " + mem[money][i]);
            return mem[money][i];
        }

        long subtotal = 0;
//         int j = 0;
        int remaining = money;
        while (remaining >= 0) {
            subtotal += dp(remaining, i + 1, coins);
            remaining -= coins[i];
//             ++j;
            // invariant: money = money (input) - j * coins[i]
        }
        // truth: j is the number of times coins[i] had been subtracted
        // from money for money to reach a value of 0 or less.

        mem[money][i] = subtotal;

//         System.out.println("calculate (i = " + i + ", money = " + money + ", subtotal = " + subtotal);
        return subtotal;
    }

    public static long makeChange(int[] coins, int money) {
        // This is a DP problem.
        /*
        Guess: For remaining sum S and the given coins in some pre-determined
        order, guess the number of these coins in the change.

        If we have reached the last coin, and it is possible to meet the sum S
        only using this coin, then return 1; otherwise, return 0.

        The top level accumulates all the return values.

        subproblem: Remaining sum S, index i for the current coin.

        recurrence: S - coins[i] * j for all j where the difference >= 0.

        time:
        number of subproblems: (S * m)
        time per subproblem: S
        total time: S^2 * m.
        Actually, it is O(2^|S| * m)

        use top-down memoization.
        */

        // use 1-based indexing for money.
        mem = new long[money+1][coins.length];
        for (int i = 0; i != money+1; ++i) {
            for (int j = 0; j != coins.length; ++j) {
                mem[i][j] = -1; // means uncalculated.
            }
        }

        return dp(money, 0, coins);
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
