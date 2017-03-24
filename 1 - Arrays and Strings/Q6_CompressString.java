import java.util.ArrayList;
public class CompressString {
    public static void main(String args[]){
	//check if args is len 1
	//how to check if it's actually a string
	String s = args[0];
	System.out.println(compressString(s));
    }
    public static String compressString(String s){
	if (s.length()<2){
	    return s;
	}
	ArrayList<Character> c = new ArrayList<Character>();
	int counter = 1;
	for (int i = 1; i < s.length(); i++){
	    if(s.charAt(i)==s.charAt(i-1)){
		counter++;
		if (i==s.length()-1){
		    c.add(s.charAt(i));
		    c.add((Character)counter);
		}
	    } else {
		c.add(s.charAt(i));
		c.add(counter);
		counter = 1;
		if (i==s.length()-1){
		    c.add(s.charAt(i));
		    c.add((Character)counter);
		}
	    }
	}
	String compressed = c.toString();
	System.out.println(compressed);
	/*if (compressed.length() < s.length()){
	    return compressed;
	    }*/
	return s;
    }
}