import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] lectures = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            lectures[i][0] = Integer.parseInt(st.nextToken()); // p: 강연료
            lectures[i][1] = Integer.parseInt(st.nextToken()); // d: 마감일
        }

        // 마감일 기준 오름차순 정렬
        Arrays.sort(lectures, (a, b) -> a[1] - b[1]);

        PriorityQueue<Integer> pq = new PriorityQueue<>(); // min-heap

        for (int i = 0; i < n; i++) {
            int pay = lectures[i][0];
            int day = lectures[i][1];

            if (pq.size() < day) {
                pq.offer(pay); // 날짜 여유 있으면 그냥 추가
            } else if (!pq.isEmpty() && pq.peek() < pay) {
                pq.poll(); // 가장 값싼 강연 제거
                pq.offer(pay); // 지금 강연 추가
            }
        }

        int result = 0;
        while (!pq.isEmpty()) {
            result += pq.poll();
        }

        System.out.println(result);
    }
}
