import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());

        // dp 배열 생성
        int[] dp = new int[N + 1];
        dp[1] = 1; // 초기값 설정

        // dp
        for (int i = 2; i <= N; i++) {
            if (i == (int) Math.sqrt(i) * Math.sqrt(i)) { // 제곱수는 1
                dp[i] = 1;
            } else { // 제곱수가 아니면 제곱수의 합으로 표현
                dp[i] = i; // 최악의 경우로 초기화
                for (int j = 1; j * j < i; j++) {
                    dp[i] = Math.min(dp[i], 1 + dp[i - j * j]);
                }
            }
        }

        // 출력
        System.out.println(dp[N]);
    }
}