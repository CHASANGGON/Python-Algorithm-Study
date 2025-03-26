import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        // 도로 길이 입력 받기
        int[] roads = new int[N - 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N - 1; i++) {
            roads[i] = Integer.parseInt(st.nextToken());
        }

        // 리터당 가격 입력 받기
        int[] oils = new int[N - 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N - 1; i++) {
            oils[i] = Integer.parseInt(st.nextToken());
        }

        // greedy
        int priceSum = oils[0] * roads[0], disSum = roads[0], minPrice = oils[0]; // 초기값 설정
        for (int i = 1; i < N - 1; i++) {
            if (oils[i] < minPrice) { // 최소 가격을 발견했다면
                minPrice = oils[i]; // 가격 갱신
            }
            priceSum += minPrice * roads[i]; // 비용 누적합
        }

        // 출력
        System.out.println(priceSum);
    }
}