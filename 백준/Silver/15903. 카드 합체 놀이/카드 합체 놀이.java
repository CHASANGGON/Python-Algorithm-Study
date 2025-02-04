import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // n, m 입력 받기
        String[] nm = br.readLine().split(" ");
        long n = Integer.parseInt(nm[0]);
        long m = Integer.parseInt(nm[1]);

        // 숫자 입력 받기
        PriorityQueue<Long> pq = new PriorityQueue<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            pq.offer((long) Integer.parseInt(st.nextToken()));
        }

        // m = 2
        // 1 2 3 4 5 6
        // 3 3 3 4 5 6
        // 3 4 5 6 6 6
        // = 30

        // m = 3
        // 1 2 3 4 5 6
        // 3 3 3 4 5 6
        // 3 4 5 6 6 6
        // 5 6 6 6 7 7
        // = 37 = 30 + 7

        // m = 4
        // 1 2 3 4 5 6
        // 3 3 3 4 5 6
        // 3 4 5 6 6 6
        // 5 6 6 6 7 7
        // 6 6 7 7 11 11
        // = 48 = 37 + 11

        // m 번 합
        for (int i = 0; i < m; i++) {
            long a = pq.poll();
            long b = pq.poll();
            long ab = a + b;
            pq.offer(ab);
            pq.offer(ab);
        }

        long ans = 0;
        while (!pq.isEmpty()) {
            ans += pq.poll();
        }

        System.out.println(ans);
    }
}