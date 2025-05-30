import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력
        int N = Integer.parseInt(st.nextToken()); // 원생의 수
        int K = Integer.parseInt(st.nextToken()); // 조의 개수

        st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> diff = new PriorityQueue<>(Collections.reverseOrder()); // 내림차순 정렬
        int now = 0, before = Integer.parseInt(st.nextToken()), start = before;
        for (int i = 0; i < N - 1; i++) {
            now = Integer.parseInt(st.nextToken());
            diff.offer(now - before);
            before = now;
        }

        int ans = before - start;
        while(K -- > 1) {
            ans -= diff.poll();
        }

        // 출력
        System.out.println(ans);
    }
}