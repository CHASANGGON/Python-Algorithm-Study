import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] lectures = new int[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            lectures[i][0] = Integer.parseInt(st.nextToken());
            lectures[i][1] = Integer.parseInt(st.nextToken());
        }
        
        // 강의를 시작시간 기준으로 정렬
        Arrays.sort(lectures, Comparator.comparingInt(a -> a[0]));

        // 우선순위 큐(최소 힙): 각 강의실의 종료 시간을 저장
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(lectures[0][1]);  // 첫 번째 강의 종료시간을 추가

        for (int i = 1; i < N; i++) {
            int start = lectures[i][0];
            int end = lectures[i][1];
            
            // 현재 가장 빨리 끝나는 강의실의 종료 시간이 강의 시작시간보다 작거나 같으면 재사용
            if (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll();
            }
            
            // 새로운 강의실에 강의 배정 혹은 기존 강의실의 종료시간 업데이트
            pq.offer(end);
        }
        
        // 필요한 강의실의 수는 우선순위 큐에 남은 강의실의 개수
        System.out.println(pq.size());
    }
}
