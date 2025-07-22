import java.io.*;
import java.util.*;

public class Main {
    private static int[][] arr = new int[10][10];
    private static int[] paperCounts = {0, 5, 5, 5, 5, 5}; // 인덱스 1부터 5까지 각 사이즈별 남은 색종이 개수
    private static int minCount = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 10; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 백트래킹 함수 호출
        // (0,0) 위치부터 시작하며, 현재까지 사용한 색종이 개수는 0
        findMinPapers(0, 0, 0);

        if (minCount == Integer.MAX_VALUE) {
            System.out.println(-1); // 모든 1을 덮을 수 없는 경우
        } else {
            System.out.println(minCount);
        }
    }

    // --- 유틸리티 함수 (이전 코드에서 가져옴) ---
    private static boolean check() { // 이 함수는 최종적으로 모든 1이 0이 되었는지 확인할 때 사용
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (arr[i][j] == 1) {
                    return false;
                }
            }
        }
        return true;
    }

    private static void cover(int row, int col, int size) {
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                arr[i][j] = 0;
            }
        }
    }

    private static void uncover(int row, int col, int size) {
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                arr[i][j] = 1;
            }
        }
    }

    private static boolean isCanCover(int row, int col, int size) {
        // 경계 조건 확인 추가
        if (row + size > 10 || col + size > 10) {
            return false;
        }
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if (arr[i][j] == 0) { // 0이 있으면 덮을 수 없음
                    return false;
                }
            }
        }
        return true;
    }

    // --- 백트래킹 재귀 함수 ---
    private static void findMinPapers(int row, int col, int currentCount) {
        // 1. 모든 칸을 다 탐색했으면 (기저 조건)
        if (col == 10) { // 한 행의 끝에 도달하면 다음 행으로
            row++;
            col = 0;
        }
        if (row == 10) { // 모든 행을 다 탐색했으면
            // 모든 1이 0으로 덮였는지 최종 확인 (선택적)
            // 백트래킹 과정에서 1이 남아있는 경우는 이 경로로 오지 못하도록 만들거나, 여기서 체크
            // 이 문제에서는 모든 1을 덮어야 하므로, 모든 1이 0이 되었는지 확인하는 check() 함수를 여기서 호출할 필요가 있음
            // 하지만 보통은 1을 찾아 덮는 과정에서 모든 1이 덮이면 성공으로 간주하고 minCount를 갱신
            // 여기서는 단순하게 currentCount가 현재까지의 minCount보다 작으면 갱신
            minCount = Math.min(minCount, currentCount);
            return;
        }

        // 2. 현재 위치가 0이면 다음 칸으로 이동
        if (arr[row][col] == 0) {
            findMinPapers(row, col + 1, currentCount);
            return;
        }

        // 3. 현재 위치가 1이면 색종이를 덮어보는 모든 경우의 수 시도
        // 가장 큰 색종이부터 덮는 것이 보통 유리 (백트래킹 가지치기에 도움)
        for (int size = 5; size >= 1; size--) {
            // 해당 size의 색종이가 남아있고, 이 위치에 덮을 수 있다면
            if (paperCounts[size] > 0 && isCanCover(row, col, size)) {
                paperCounts[size]--; // 색종이 사용
                cover(row, col, size); // 덮기

                findMinPapers(row, col + 1, currentCount + 1); // 다음 칸으로 이동하여 재귀 호출

                // 백트래킹: 사용했던 색종이를 되돌리고, 덮었던 영역을 다시 1로
                uncover(row, col, size);
                paperCounts[size]++;
            }
        }
    }
}