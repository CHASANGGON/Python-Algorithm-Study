import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        int N = Integer.parseInt(br.readLine()), minusCnt = 0;
        long[] arr = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            long num = Integer.parseInt(st.nextToken());
            arr[i] = num;
            if (num < 0) minusCnt++;
        }

        if (minusCnt == 0) { // 양수만 존재하는 경우
            System.out.println(arr[0] + " " + arr[1]);
        } else if (minusCnt == N) { // 음수만 존재하는 경우
            System.out.println(arr[N - 2] + " " + arr[N - 1]);
        } else { // 양수 음수 모두 존재하는 경우 -> 이분 탐색 필요
            int left = 0, right = N - 1;
            long ans1 = 0, ans2 = 0;
            long minSum = 1000000000, sum = 1000000000;

            while (sum != 0 && left < right) {
                sum = arr[left] + arr[right];
                if(Math.abs(sum) < minSum) {
                    minSum = Math.abs(sum);
                    ans1 = arr[left];
                    ans2 = arr[right];
                }
                if (sum > 0) right--;
                else if (sum < 0) left++;
            }
            System.out.println(ans1 + " " + ans2);
        }
    }
}