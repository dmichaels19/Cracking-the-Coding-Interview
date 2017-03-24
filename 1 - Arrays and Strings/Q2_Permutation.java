import java.util.Arrays;
public class Permutation {
    public static void main(String[] args){
	if (args.length != 2){
	    System.out.println("Not two arguments");
	    return;
	}
	String str1 = args[0];
	String str2 = args[1];
	System.out.println(isPermutation(str1,str2));
    }
    public static boolean isPermutation(String str1, String str2){
	char[] chars1 = str1.toCharArray();
	char[] chars2 = str2.toCharArray();
	Arrays.sort(chars1);
	Arrays.sort(chars2);
	str1 = new String(chars1);
	str2 = new String(chars2);
	return str1.equals(str2);
    }
}