import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N, M 입력 받기
        int N = Integer.parseInt(br.readLine()); // 사람의 수
        int K = Integer.parseInt(br.readLine()); // 파티의 수

        // 이분 탐색
        long ans = 0;
        long left = 1;
        long right = (long) N * N;

        while (left <= right) {
            long cnt = 0;
            long mid = (left + right) / 2;

            for (long i = 1; i <= N; i++) {
                cnt += Math.min(mid / i, N);
            }

            if (cnt < K) left = mid + 1;
            else {
                ans = mid;
                right = mid - 1; // 같은 값을 갖는 더 작은 인덱스의 수가 있는지 찾아야함
            }
        }

        System.out.println(ans);
    }
}