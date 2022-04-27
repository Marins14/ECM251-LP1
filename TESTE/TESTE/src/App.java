import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner (System.in);
        int n = in.nextInt();
        System.out.println(Func(n));
        in.close();
    }
    public static int Func(int n){
        int m=0;
        int i=1;
        while (i<= n){
            m = m +1;
            i = i*2;
        }
        return m;
    }
}

