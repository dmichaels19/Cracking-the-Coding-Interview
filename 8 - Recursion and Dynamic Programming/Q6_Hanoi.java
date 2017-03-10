import java.util.Stack;

public class Hanoi {
  public static void main (String[] args) {
    if (args.length != 1) {
      System.out.println("Usage: java hanoi -n\nwhere n is number of elements");
    }
    int n = Integer.parseInt(args[0]);
    System.out.println(n);
    Stack<Integer> A = new Stack<Integer>();
    Stack<Integer> B = new Stack<Integer>();
    Stack<Integer> C = new Stack<Integer>();
    for (int i = n; i > 0; i--) {
      A.push(new Integer(i));
      System.out.println(i + " pushed to Stack A");
    }
    double start = System.nanoTime();
    hanoi(n,A,B,C);
    for (int i = n; i > 0; i--) {
      System.out.println(C.pop());
    }
    System.out.println(System.nanoTime() - start);
  }
  static void hanoi (int n, Stack<Integer> l, Stack<Integer> m, Stack<Integer> r) {
    if (n==0) {
      return;
    }
    hanoi (n-1, l, r, m);
    r.push(l.pop());
    hanoi (n-1, m, l, r);
  }
}
