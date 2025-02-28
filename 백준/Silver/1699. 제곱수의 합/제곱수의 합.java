import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());

        // dp 배열 생성
        int[] dp = new int[N + 1];

        // dp
        // 제곱수는 모두 1
        for (int i = 1; i <= (int) Math.sqrt(N); i++) {
            dp[i * i] = 1;
        }

        // 제곱수들의 합
        for (int i = 1; i < (int) Math.sqrt(N); i++) {
            for (int j = 1; j < (int) Math.sqrt(N); j++) {
                int target = i * i + j * j;
                if (target <= N && dp[target] == 0) {
                    dp[target] = 2;
                }
            }
        }

        // 탐색
        for (int i = 3; i <= N; i++) {
            if (dp[i] == 0) {
                dp[i] = Integer.MAX_VALUE;
                for (int j = 1; j <= (i + 1) / 2; j++) {
                    dp[i] = Math.min(dp[i], dp[j] + dp[i - j]);
                }
            }
        }

        // 디버깅
//        for (int i = 1; i <= N; i++) {
//            System.out.print(dp[i] + " ");
//        }

        // 출력
        System.out.println(dp[N]);
    }
}