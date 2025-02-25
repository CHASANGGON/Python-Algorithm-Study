import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // T 입력 받기
        int T = Integer.parseInt(br.readLine());

        // DP 배열 생성
        int[] dp1 = new int[41], dp2 = new int[41];
        dp1[0] = 1;
        dp2[1] = 1;
        for (int i = 2; i < 41; i++) {
            dp1[i] = dp1[i - 1] + dp1[i - 2];
            dp2[i] = dp2[i - 1] + dp2[i - 2];
        }

        // 테스트 케이스 입력 받기
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            sb.append(dp1[N]).append(" ").append(dp2[N]).append("\n");
        }

        // 출력
        System.out.println(sb);
    }
}