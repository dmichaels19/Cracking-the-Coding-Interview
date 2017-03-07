/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg8.pkg9.parens;

/**
 *
 * @author David
 */
public class Parens {
    static int total;
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        recurse(4, 0, "");
        System.out.println(total);
        
//        double last = 1;
//        for (int i = 1; i < 20; i++) {
//            total = 0;
//            double start = System.nanoTime();
//            recurse(i, 0, "");
//            double difference = (System.nanoTime() - start);
//            
//            System.out.println(difference / last);
//            last = difference;
//            //System.out.println();
//            //System.out.println("Number " + i + ": " + total);
//        }
        
    }
    
    static void recurse(int opensToGo, int numOpened, String s){
        if (opensToGo == 0){
            if(numOpened == 0){
                //System.out.print(s + ", ");
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
