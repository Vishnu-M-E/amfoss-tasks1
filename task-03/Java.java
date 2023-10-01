import java.util.*;

public class Main {
    public static void main(String[] args) {
      Scanner obj=new Scanner(System.in);
      int n=obj.nextInt();
      int i,j;
      System.out.println(2);
      System.out.println(3);
      for (i=4;i<=n;i++){
        for (j=2;j<=i/2;j++){
          if (i%j==0){
            break;
          }
        }
        if (i%j!=0){
          System.out.println(i);
        }
      }
  }
}