  /*
  * Write a method to replace all spaces in a string with'%20'. 
  * You may assume that the string has sufficient space at the 
  * end of the string to hold the additional characters, and that 
  * you are given the "true" length of the string. 
  * (Note: if implementing in Java, please use a character array 
  * so that you can perform this operation in place.)

  * EXAMPLE
  *  Input:  "Mr John Smith    "
  *  Output: "Mr%20John%20Smith"
  */

public class Q3_Spaces{
    
  public static void main(String[] args){
    System.out.println(spaces("Mr. John Smith    ", 14));

  }

  public static char[] spaces(String input, int trueLength){
    char[] c = input.toCharArray();
    int i = trueLength -1;
    int j = c.length - 1;

    while(i != j){
      System.out.println("i= "+ i + ": " +c[i]);
      System.out.println("j= " + j + ": "+ c[j]);
      if(c[i] == ' '){
        c[j] = '0';
        c[--j] = '2';
        c[--j] = '%';
      }

      else {
        c[j] = c[i];
      }

      i--;
      j--;
    }

    return c;
  }

}
