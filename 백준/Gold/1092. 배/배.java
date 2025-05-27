import java.io.*;
import java.util.*;

public class Main {
    private static int N, M;
    private static int[] crane;
    private static List<Integer> boxes;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 크레인 입력
        N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        crane = new int[N];
        for (int i = 0; i < N; i++) {
            crane[i] = Integer.parseInt(st.nextToken());
        }

        // 박스 입력
        M = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        boxes = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            boxes.add(Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(crane); // 크레인 오름차순 정렬
        boxes.sort(Collections.reverseOrder()); // 박스 내림차순 정렬

        solve();
    }

    private static void solve() {


        if (crane[N - 1] < boxes.get(0)) { // 제일 큰 크레인보다 박스가 무거우면 불가능
            System.out.println(-1);
            return;
        }

        int cnt = 0;
        while (!boxes.isEmpty()) {
            cnt++;

            int size = boxes.size();

            // 크레인으로 박스 제거
            int craneIdx = N - 1;
            int boxIdx = 0;
            while (craneIdx >= 0 && boxIdx < boxes.size()) { // 크레인 한 개당

                if (boxes.get(boxIdx) <= crane[craneIdx]) {
                    boxes.remove(boxIdx);
                    craneIdx--; // 현재 크레인 사용 완료
                } else {
                    boxIdx++; // 현재 크레인 재사용, 다음 박스
                }
            }

            // 박스가 모두 제거됐다면 종료
            if (boxes.isEmpty()) {
                System.out.println(cnt);
                return;
            }
        }

    }

}