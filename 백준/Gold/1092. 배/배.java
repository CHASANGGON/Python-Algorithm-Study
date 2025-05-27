import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        Integer[] crane = new Integer[N];
        for (int i = 0; i < N; i++) {
            crane[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        List<Integer> boxes = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            boxes.add(Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(crane, Collections.reverseOrder()); // 내림차순
        boxes.sort(Collections.reverseOrder());         // 내림차순

        // 제일 무거운 박스를 가장 센 크레인도 못 들면 불가능
        if (boxes.get(0) > crane[0]) {
            System.out.println(-1);
            return;
        }

        int time = 0;

        while (!boxes.isEmpty()) {
            int boxIdx = 0;
            for (int i = 0; i < N;) {
                if (boxIdx >= boxes.size()) break;

                if (crane[i] >= boxes.get(boxIdx)) {
                    boxes.remove(boxIdx); // 현재 크레인이 들 수 있는 박스 제거
                    i++; // 다음 크레인
                } else {
                    boxIdx++; // 현재 박스를 다음 크레인에게 시도
                }
            }
            time++;
        }

        System.out.println(time);
    }
}
