import java.io.*;
import java.util.*;

class Main {
    static int N, M, islandCount, checkCount = 0, minLen = 0;
    static int[] di = {1, -1, 0, 0}, dj = {0, 0, 1, -1}, parent;
    static int[][] map;
    static List<int[]> islands;
    static List<int[]>[] labeled;
    static PriorityQueue<int[]> bridgeCandidate;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N, M 입력 받기
        N = Integer.parseInt(st.nextToken()); // 가로
        M = Integer.parseInt(st.nextToken()); // 세로

        // 자료 구조 생성
        map = new int[N][M];
        islands = new ArrayList<>();

        // 지도 입력 받기
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int spcae = Integer.parseInt(st.nextToken());
                if (spcae == 1) {
                    islands.add(new int[]{i, j});
                }
                map[i][j] = spcae;
            }
        }

        // 1. 섬 라벨링
        labeling();

        // 1. 라벨링 디버깅
        //print();

        // 2. 섬 -> 섬 다리 연결(pq에 저장, 섬번호(from, to)와 길이를 저장)
        bridgeCandidate = new PriorityQueue<>((a, b) -> Integer.compare(a[2], b[2])); // default값은 오름차순 정렬
        registerBridgeCandidate(); // 가능한 다리 정보들을 후보로 등록

        // 3. 짧은 순으로 연결
        connect();

        // 4. 최종 검사 및 출력
        if (islandCount - 1 == checkCount) { // MST는 "노드의 개수 - 1 = 간선의 개수"를 만족
            System.out.println(minLen);
        } else {
            System.out.println(-1);
        }

    }

    private static int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
            return parent[x];
        }
        return parent[x];
    }

    private static boolean union(int a, int b) {
        int pa = find(a);
        int pb = find(b);

        if (pa == pb) return false;

        parent[pb] = pa;
        return true;
    }

    private static void connect() {
        parent = new int[islandCount + 1];
        for (int i = 1; i <= islandCount; i++) {
            parent[i] = i;
        }

        while (!bridgeCandidate.isEmpty()) { // 길이가 짧은 다리부터 고려
            int[] info = bridgeCandidate.poll();

            int from = info[0];
            int to = info[1];
            int len = info[2];

            if (from > to) { // from <= to 가 되도록 유지(우측 상단 반틈만 visited로 사용)
                int temp = from;
                from = to;
                to = temp;
            }

            if (union(from, to)) { // from과 to의 부모가 다르다면 -> 연결되지 않은 것
//                System.out.println("from " + from + " to " + to + " len " + len);
                minLen += len;
                checkCount++;
            }
        }
    }

    private static void registerBridgeCandidate() {

        for (int[] info : islands) { // 모든 섬 좌표에서 검사해야 함
            int i = info[0];
            int j = info[1];

            int from = map[i][j];
            int islandNum = map[i][j];

            // 네 방향에 대해서 다리를 이어보기
            for (int dir = 0; dir < 4; dir++) {
                int ni = i;
                int nj = j;
                int len = 0; // 다리의 길이

                while (true) {
                    ni += di[dir];
                    nj += dj[dir];

                    // 인덱스를 벗어나면 탈출
                    if (ni < 0 || ni >= N || nj < 0 || nj >= M) break;

                    // 바다를 만나면
                    if (map[ni][nj] == 0) {
                        len++; // 길이 증가
                    } else { // 섬을 만났다면
                        // 다른 섬이라면
                        if (map[ni][nj] != islandNum && len >= 2) { // 길이 2이상인 다리만 연결
                            int to = map[ni][nj];
                            bridgeCandidate.offer(new int[]{from, to, len}); // 후보에 등록
                        }
                        break; // 자기 섬을 다시 만나거나 길이가 1인 다리
                    }
                }
            }
        }
    }

    private static void print() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static void labeling() {
        boolean[][] visited = new boolean[N][M];
        int label = 1;

        for (int[] info : islands) {
            int i = info[0];
            int j = info[1];

            if (!visited[i][j]) {
                visited[i][j] = true;
                map[i][j] = label;

                Queue<int[]> q = new LinkedList<>();
                q.offer(new int[]{i, j});

                while (!q.isEmpty()) {
                    int[] cur = q.poll();

                    for (int dir = 0; dir < 4; dir++) {
                        int ni = cur[0] + di[dir];
                        int nj = cur[1] + dj[dir];

                        if (ni >= 0 && ni < N && nj >= 0 && nj < M && map[ni][nj] == 1 && !visited[ni][nj]) {
                            map[ni][nj] = label;
                            visited[ni][nj] = true;
                            q.offer(new int[]{ni, nj});
                        }
                    }
                }

                label++;
            }
        }

        islandCount = label - 1; // 섬 개수 저장
    }
}