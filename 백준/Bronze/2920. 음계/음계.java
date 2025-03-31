import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int start = Integer.parseInt(st.nextToken());
        if (start == 1) {
            int cnt = 1;
            for (int i = 0; i < 7; i++) {
                if (Integer.parseInt(st.nextToken()) != ++cnt)  {
                    System.out.println("mixed");
                    return;
                };
            }
            System.out.println("ascending");
        } else if (start == 8) {
            int cnt = 8;
            for (int i = 0; i < 7; i++) {
                if (Integer.parseInt(st.nextToken()) != --cnt)  {
                    System.out.println("mixed");
                    return;
                };
            }
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }
    }
}
