import java.io.*;
import java.util.*;

public class Main {
    private static int N;
    private static char[] from1, from2, to;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력
        N = Integer.parseInt(br.readLine());

        // 배열 생성
        from1 = new char[N];
        from2 = new char[N];

        // 초기 전구 입력
        String line = br.readLine();
        for (int i = 0; i < N; i++) {
            from1[i] = from2[i] = line.charAt(i);
        }

        // 완성할 전구 입력
        to = new char[N];
        line = br.readLine();
        for (int i = 0; i < N; i++) {
            to[i] = line.charAt(i);
        }

        // greedy
        int cnt1 = greedy(from1, 0); // 첫 번째 전구

        toggle(from2, 0); // 첫 번째 스위치를 누른 경우
        int cnt2 = greedy(from2, 1); // 두 번째 전구

        // 출력
        int ans = -1;
        if (check(from1)) ans = cnt1;
        if (check(from2)) ans = Math.min(cnt2, ans == -1 ? cnt2 : ans);
        System.out.println(ans);
    }

    private static boolean check(char[] from) {
        for (int i = 0; i < N; i++) {
            if (from[i] != to[i]) {
                return false;
            }
        }
        return true;
    }

    private static void toggle(char[] from, int i) {
        for (int j = i - 1; j <= i + 1; j++) {
            if (j >= 0 && j < N) {
                from[j] = from[j] == '0' ? '1' : '0';
            }
        }
    }

    private static int greedy(char[] from, int cnt) {
        for (int i = 1; i < N; i++) {
            if (from[i - 1] != to[i - 1]) {
                toggle(from, i);
                cnt++;
            }
        }
        return cnt;
    }
}