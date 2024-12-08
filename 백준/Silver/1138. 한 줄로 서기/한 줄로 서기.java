import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        int[] ans = new int[n]; // 결과 배열 (0으로 초기화)

        for (int i = 0; i < n; i++) {
            int count = arr[i]; // 왼쪽에 있어야 하는 키 큰 사람 수
            for (int j = 0; j < n; j++) {
                if (ans[j] == 0) { // 비어있는 자리 찾기
                    if (count == 0) {
                        ans[j] = i + 1; // 현재 사람 (i + 1) 배치
                        break;
                    }
                    count--;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print(ans[i] + " ");
        }
    }
}
