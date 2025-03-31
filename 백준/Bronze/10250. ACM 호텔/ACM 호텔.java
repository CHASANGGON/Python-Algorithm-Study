import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            int y = (N - 1) % H + 1; // 층수 (Y)
            int x = (N - 1) / H + 1; // 호수 (X)

            System.out.printf("%d%02d\n", y, x); // 1~9호는 01, 02처럼 출력
        }
    }
}
