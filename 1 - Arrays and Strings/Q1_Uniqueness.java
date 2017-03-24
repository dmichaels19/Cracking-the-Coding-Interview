import java.util.Arrays;
public class Uniqueness {
    public static void main(String args[]){
	if (args.length!=1){
	    System.out.println("Need argument");
	}
	String str1 = args[0];
	char[] chars = str1.toCharArray();
	Arrays.sort(chars);
	str1 = new String(chars);
	System.out.println(isUnique(str1));
    }
    public static boolean isUnique(String str1){
	for (int i=1; i<str1.length(); i++){
	    if (str1.charAt(i)==str1.charAt(i-1)){
		return(false);
	    }
	}
	return(true);
    }
}