import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 배열 입렫 받기
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // DP(누적합)
        int[] dp = new int[N];
        dp[0] = arr[0];
        for (int i = 1; i < N; i++) {
            dp[i] = dp[i - 1] + arr[i];
        }


        // 출력
        for (int k = 0; k < M; k++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken()) - 2;
            int j = Integer.parseInt(st.nextToken()) - 1;
            if (i == -1) {
                System.out.println(dp[j]);
            } else {
                System.out.println(dp[j] - dp[i]);
            }
        }
    }
}