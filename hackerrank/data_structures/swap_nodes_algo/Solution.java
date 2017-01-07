import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static Map<Integer, Node> nodeMap = new HashMap<>();

    public static Node getNodeFromMap(int index) {
        if (index == -1) {
            return null;
        }

        if (nodeMap.containsKey(index)) {
            return nodeMap.get(index);
        } else {
            Node newNode = new Node();
            newNode.index = index;
            nodeMap.put(index, newNode);
            return newNode;
        }
    }

    public static void swapAux(Node node, int d, int k) {
        if (node == null) {
            return;
        }

        if (d % k == 0) {
            Node tmp = node.left;
            node.left = node.right;
            node.right = tmp;
        }
        swapAux(node.left, d + 1, k);
        swapAux(node.right, d + 1, k);
    }

    public static void swap(int k) {
        Node root = nodeMap.get(1);
        swapAux(root, 1, k);
    }

    public static void printInOrderAux(Node node) {
        if (node == null) {
            return;
        }
        printInOrderAux(node.left);
        System.out.print(node.index + " ");
        printInOrderAux(node.right);
    }

    public static void printInOrder() {
        Node root = nodeMap.get(1);
        printInOrderAux(root);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 1; i <= n; ++i) {
            int l = scanner.nextInt(), r = scanner.nextInt();
//             System.out.println("attaching " + l + " and " + r + " to " + i);
            Node ele = getNodeFromMap(i);
            // Establish the left and right nodes.
            ele.left = getNodeFromMap(l);
            ele.right = getNodeFromMap(r);
        }

        n = scanner.nextInt();
        int k;
        for (int i = 0; i != n; ++i) {
            k = scanner.nextInt();
            swap(k);
            printInOrder();
            System.out.println();
        }
    }
}

class Node {
    int index;
    Node left, right;
}
