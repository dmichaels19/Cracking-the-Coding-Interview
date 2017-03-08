    /*
     * 8.9 Parens: Implement an algorithm to print all valid 
     * (e.g., properly opened and closed) combinations of n pairs of parentheses.
    
     * EXAMPLE
     * Input: 3
     * Output: ((())), (()()), (())(), ()(()), ()()()
     */

public class Q9_Parens {
    
    static int total;

    public static void main(String[] args) {
        // TODO code application logic here
        if (args.length != 1) {
            System.out.println("Usage: java Parentheses -n\nwhere n is number of elements");
        }
        total = 0;
        int n = Integer.parseInt(args[0]);
        recurse(n, 0, "");
        
        //Total number of parentheses combinations
        System.out.println(total);
        
    }
    
    // opensToGo starts as the number of parentheses to use
    // numOpened refers to the number of brackets that have been opened but not closed
    static void recurse(int opensToGo, int numOpened, String s){
        //If N parentheses have been opened
        if (opensToGo == 0){
            if(numOpened == 0){
                System.out.print(s + ", ");
                total++;
            } else {
                recurse(opensToGo, numOpened-1, s + ")");
            }
        } else {
            if (numOpened > 0){
                recurse(opensToGo, numOpened-1, s + ")");
                recurse(opensToGo-1, numOpened+1, s + "(");
            } else {
                recurse(opensToGo-1, numOpened+1, s + "(");
            }
        }
    }
    
}
