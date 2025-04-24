import java.io.*;
import java.util.*;

public class Main {
    static int cnt = 0, M, N;
    static int[] di = {0, 0, 1, -1}, dj = {1, -1, 0, 0};
    static int[][] map, dp;
    static Stack<int[]> stack = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N, M 입력 받기
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        map = new int[M][N];
        dp = new int[M][N];

        // 지도 입력 받기
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }

        // dfs + dp && 출력
        System.out.println(dfs(0, 0));
    }

    private static int dfs(int i, int j) {
        // 종료 조건
        if (i == M - 1 && j == N - 1) {
            return 1;
        }

        // 백트래킹
        if (dp[i][j] != -1) return dp[i][j];
        
        dp[i][j] = 0;

        // dfs
        for (int d = 0; d < 4; d++) {
            int ni = i + di[d];
            int nj = j + dj[d];

            if (ni >= 0 && ni < M && nj >= 0 && nj < N && map[i][j] > map[ni][nj]) {
                dp[i][j] += dfs(ni, nj); // 재귀
            }
        }

        return dp[i][j];
    }
}