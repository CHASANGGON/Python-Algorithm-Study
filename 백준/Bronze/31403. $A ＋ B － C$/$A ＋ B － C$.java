import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        // 출력1
        System.out.println(A + B - C);

        // 출력2
        String AB = String.valueOf(A) + String.valueOf(B);
        System.out.println(Integer.parseInt(AB) - C);
    }
}
