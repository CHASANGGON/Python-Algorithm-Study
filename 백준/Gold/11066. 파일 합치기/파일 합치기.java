import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {

            int K = Integer.parseInt(br.readLine());
            int[] files = new int[K + 1];
            int[] sum = new int[K + 1];
            int[][] dp = new int[K + 1][K + 1];

            StringTokenizer st = new StringTokenizer(br.readLine());

            // 파일 크기 입력 받기
            for (int i = 1; i <= K; i++) {
                files[i] = Integer.parseInt(st.nextToken());
                sum[i] = sum[i - 1] + files[i];
            }

            // DP
            for (int length = 2; length <= K; length++) { // 길이를 증가시키면 답을 만들어갈 것임(이게 DP 방식)
                for (int start = 1; start <= K - length + 1; start++) { // start ~ end 구간을 하나씩 갱신
                    int end = start + length - 1;

                    dp[start][end] = Integer.MAX_VALUE; // 갱신 대상

                    for (int divLine = start; divLine < end; divLine++) { // (start ~ end)에서 자르는 기준 점
                        // 길이 4를 예로 들면, 
                        // (1,3) or (2,2) or (3,1) 로 잘라서 합친 것 중에서 
                        // 최댓값으로 갱신
                        dp[start][end] = Math.min(dp[start][end], dp[start][divLine] + dp[divLine + 1][end] + sum[end] - sum[start - 1]);
                    }
                }
            }

            // 출력
            System.out.println(dp[1][K]);
        }
    }
}