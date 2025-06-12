import java.io.*;
import java.util.*;

public class Main {
    private static int R, C, ans = 0;
    private static char[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // R, C 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        // 맵 입력
        map = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        // 모든 행에서 출발
        for (int r = 0; r < R; r++) {
            greedyDfs(r, 0);
        }

        // 출력
        System.out.println(ans);
    }

    private static boolean greedyDfs(int r, int c) {
        // 마지막 열에 도달하면 성공
        if (c == C - 1) {
            ans++;
            return true;
        }

        // 현재 위치 방문 표시
        map[r][c] = 'p';

        // 그리디: 위쪽부터 탐색 (-1, 0, 1 순서)
        for (int dr = -1; dr <= 1; dr++) {
            int nr = r + dr;
            int nc = c + 1;

            // 범위 체크 및 갈 수 있는 곳인지 확인
            if (nr >= 0 && nr < R && map[nr][nc] == '.') {
                if (greedyDfs(nr, nc)) {
                    return true; // 성공하면 즉시 종료 (복구 안 함!)
                }
            }
        }

        // 여기서 복구하지 않음 - 이게 핵심!
        // 실패한 경로는 'p'로 막혀있어서 다른 경로에서 재사용 불가
        return false;
    }
}