import java.io.*;
import java.util.*;

public class Main {
    private static int i, left, right, mid;
    private static StringTokenizer st;
    private static boolean isFind;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // A, B 입력 받기
        String[] AB = br.readLine().split(" ");
        int A = Integer.parseInt(AB[0]);
        int B = Integer.parseInt(AB[1]);

        // 집합 A 입력 받기
        st = new StringTokenizer(br.readLine());
        int[] setA = new int[A];
        for (i = 0; i < A; i++) {
            setA[i] = Integer.parseInt(st.nextToken());
        }


        // 집합 B 입력 받기
        st = new StringTokenizer(br.readLine());
        int[] setB = new int[B];
        for (i = 0; i < B; i++) {
            setB[i] = Integer.parseInt(st.nextToken());
        }

        // 정렬
        Arrays.sort(setA);
        Arrays.sort(setB);

        // A - B
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for (i = 0; i < A; i++) {
            left = 0;
            right = B - 1;
            isFind = false;

            while (left <= right) {
                mid = (left + right) / 2;
                if (setA[i] == setB[mid]) {
                    isFind = true;
                    break;
                } else if (setA[i] < setB[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            if (!isFind) {
                sb.append(setA[i]).append(" ");
                cnt++;
            }
        }

        // 출력
        System.out.println(cnt); // 크기
        if (cnt > 0) {
            System.out.println(sb.toString().trim());
        }
    }
}