import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // T 입력 받기
        int T = Integer.parseInt(br.readLine());

        // DP
        int[] dp1 = new int[41], dp2 = new int[41];
        dp1[0] = 1;
        dp2[1] = 1;
        for (int i = 2; i < 41; i++) {
            dp1[i] = dp1[i - 1] + dp1[i - 2];
            dp2[i] = dp2[i - 1] + dp2[i - 2];
        }

        // 배열 입력: dp 배열에 누적합으로 바로 저장
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            bw.write(dp1[N] + " " + dp2[N] + "\n");
        }

        bw.flush();
        bw.close();
    }
}