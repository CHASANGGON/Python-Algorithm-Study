import java.io.*;
import java.util.*;

public class Main {
    static int[] board, portal;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N, M 입력 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 배열 생성
        board = new int[101]; // 이동 정보를 저장할 배열
        portal = new int[101]; // 이동 정보를 저장할 배열

        // 사다리, 뱀 입력 받기
        for (int i = 0; i < N + M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            portal[start] = end;
        }

        // bfs
        bfs(1, 0);

        // 출력
        System.out.println(board[100]);
    }

    private static void bfs(int start, int startCount) {

        // Queue 생성 및 세팅
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{start, startCount});

        while (!queue.isEmpty()) {
            int[] info = queue.poll();
            int now = info[0];
            int count = info[1];

            for (int dice = 1; dice <= 6; dice++) {
                int next = now + dice;
                if (next <= 100 && board[next] == 0) { // 방문하지 않았다면
                    board[next] = count + 1; // 방문 처리
                    if (portal[next] != 0) { // 포탈이 존재한다면
                        next = portal[now + dice];
                        board[next] = count + 1; // 추가 방문 처리
                    }
                    queue.offer(new int[]{next, count + 1});
                }
            }
        }
    }
}