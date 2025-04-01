import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // T 입력 받기
        int T = Integer.parseInt(br.readLine());

        // 테스트 케이스
        while (T-- > 0) {
            int k = Integer.parseInt(br.readLine()); // 층
            int n = Integer.parseInt(br.readLine()); // 호

            int[][] apt = new int[k + 1][n + 1];

            // 0층 초기화: 1호 ~ n호까지 산다
            for (int j = 1; j <= n; j++) {
                apt[0][j] = j;
            }

            // 1층부터 k층까지 계산
            for (int i = 1; i <= k; i++) {
                for (int j = 1; j <= n; j++) {
                    apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
                }
            }

            // 출력: k층 n호
            System.out.println(apt[k][n]);
        }
    }
}
