import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;

public class Parentheses {
  public static void main (String[] args) {
    if (args.length != 1) {
      System.out.println("Usage: java Parentheses -n\nwhere n is number of elements");
    }
    int n = Integer.parseInt(args[0]);
    ArrayList<ArrayList<Double>> results = new ArrayList<ArrayList<Double>>();
    for(int cycle = 1; cycle < n; cycle++){
      for(int fuck = 0; fuck < 10; fuck++){
        results.add(new ArrayList<Double>());
        find(cycle, results);

      }
    }
    for(int cycle = 1; cycle < n; cycle++){
      double average = 0;
      for (Double result : results.get(cycle-1)) {
        average += result;
      }
      average /= results.get(cycle-1).size();
      System.out.println(average);
    }
  }
  public static void find(int n, ArrayList<ArrayList<Double>> results) {
    long start = System.nanoTime();
    HashMap<Integer,HashSet<String>> map = new HashMap<Integer,HashSet<String>>();
    HashSet<String> one = new HashSet<String>();
    one.add("()");
    map.put(new Integer(1),one);
    //is i in the map as a ket yet?
    for (int i=2;i<=n;i++){
      //System.out.println(i);
      HashSet<String> prevSet = map.get(i-1);
      map.put(i,new HashSet<String>());
      for (String value : prevSet) {
        map.get(i).add("(" + value + ")");
      }
      int j = i - 1;
      int k;
      while (j*j >= i || (j==1 && i==2)) {
        k = i - j;
        if (k==j){
          for (String value : map.get(j)) {
            map.get(i).add(value + value);
          }
        } else {
          for (String value : map.get(j)) {
            for (String value2 : map.get(k)) {
              map.get(i).add(value + value2);
              map.get(i).add(value2 + value);
            }
          }
        }
        j--;
      }
    }

    results.get(n-1).add((double)(System.nanoTime() - start)/1000000);
    //printResults(map);
  }
  public static void printResults(HashMap<Integer,HashSet<String>> map){
    for (Integer key : map.keySet()) {
      System.out.print (key + ": ");
      for (String value : map.get(key)) {
        System.out.print (value + ", ");
      }
      System.out.println();
    }
    //System.out.print(n);
  }
}
