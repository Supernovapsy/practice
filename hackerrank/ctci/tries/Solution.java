// 69 minutes, including learning things about Java's default initialization.
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Trie trie = new Trie();
        for (int a0 = 0; a0 < n; a0++){
            String op = in.next();
            String contact = in.next();
            if (op.equals("add")) {
                trie.add(contact);
            } else {
                System.out.println("" + trie.find(contact));
            }
        }
    }
}

class Trie {
    private TrieNode head = new TrieNode('\n');
    public Trie() { }

    public void add(String str) {
        head.add(str, 0);
    }

    public int find(String str) {
        return head.find(str, 0);
    }
}

class TrieNode {
    private char c;
    private int leaves;
    private HashMap<Character, TrieNode> successors;

    TrieNode(char c) {
        this.c = c;
        successors = new HashMap<Character, TrieNode>();
    }

    int find(String str, int index) {
        if (str.length() == index) {
            return leaves;
        }
        char current_char = str.charAt(index);
        if (successors.containsKey(current_char)) {
            return successors.get(current_char).find(str, index + 1);
        }
        return 0;
    }

    void add(String str, int index) {
        if (str.length() == index) {
            successors.put('$', null);
        } else {
            char current_char = str.charAt(index);
            if (successors.containsKey(current_char)) {
                successors.get(current_char).add(str, index + 1);
            } else {
                // Since this character of the string is not found at this
                // point in the trie, meaning this string is not stored in the
                // trie, create the rest of the string recursively at this
                // node.
                this.extend(str, index);
            }
        }
        ++leaves;
    }

    /** Create the rest of the string from the given index in the trie starting
     * at this node. */
    void extend(String str, int index) {
        if (str.length() == index) {
            // Once we have created the string inside the trie, we need to mark
            // the '$' to show that this is a word.
            successors.put('$', null);
        } else {
            char current_char = str.charAt(index);
            TrieNode newNode = new TrieNode(current_char);
            successors.put(current_char, newNode);
            newNode.extend(str, index + 1);
        }
        // If this is a newly created node, then initialize the leaf count to
        // 1.
        if (leaves == 0) {
            leaves = 1;
        }
    }

}
