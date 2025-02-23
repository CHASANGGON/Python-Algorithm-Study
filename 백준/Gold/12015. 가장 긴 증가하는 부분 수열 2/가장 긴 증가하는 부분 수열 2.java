import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] A;
    static ArrayList<Integer> LIS = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        N = Integer.parseInt(br.readLine());
        A = new int[N]; // 배열 생성

        // 배열 입력 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        // LIS 배열을 유지하면서 처리
        for (int num : A) {
            int idx = lowerBound(LIS, num);

            if (idx == LIS.size()) { // 가장 큰 값이면 배열의 끝에 추가
                LIS.add(num);
            } else { // lower_bound 위치에 있는 값을 교체
                LIS.set(idx, num);
            }
        }

        // 출력
        System.out.println(LIS.size()); // LIS 배열의 크기가 정답
    }

    /** 입력된 LIS 배열을 이분 탐색해서 값이 들어갈 인덱스를 반환해주는 함수 (lower_bound) **/
    private static int lowerBound(ArrayList<Integer> arr, int target) {
        int left = 0, right = arr.size();

        while (left < right) {
            int mid = (left + right) / 2;
            
            if (arr.get(mid) >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left; // target이 들어갈 위치 반환
    }
}
