import java.util.*;
public class PermOfPal {
    public static void main(String args[]){
	if (args.length != 1){
	    System.out.println("Need exactly one argument");
	}
	System.out.println(isPermOfPal(args[0]));
    }
    public static boolean isPermOfPal(String s){
	char[] c = s.toCharArray();
	Arrays.sort(c);
	s = new String(c);
	return canBePal(s);
    }
    public static boolean canBePal(String s){
	HashMap<Character, Integer> map = new HashMap<Character, Integer>();
	char[] chars = s.toCharArray();
	for (char c : chars){
	    if(!map.containsKey(c)){
		map.put(c,1);
	    } else {
		map.put(c,map.get(c));
	    }
	}
	if (chars.length%2==0){
	    for (int value : map.values()){
		if(value%2!=0){
		    return false;
		}
	    }
	    return true;
	} else {
	    boolean oddEncountered = false;
	    for (int value : map.values()){
		if(value%2!=0){
		    if(oddEncountered){
			return false;
		    } else {
			oddEncountered = true;
		    }
		} else {
		    return false;
		}
	    }
	    return true;
	}
    }
}
