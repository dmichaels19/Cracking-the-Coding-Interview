import java.util.Arrays;

public class StringRotation {
    public static void main(String[] args){
	System.out.println(isRotation(args[0],args[1]));
    }
    public static boolean isRotation(String s1, String s2){
	s2 = s2 + s2;
	return s2.contains(s1);
    }
}