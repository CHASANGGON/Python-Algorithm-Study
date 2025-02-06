import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입출력을 위한 BufferedReader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 집합 A와 B의 원소 개수 입력 받기
        int nA = Integer.parseInt(st.nextToken());
        int nB = Integer.parseInt(st.nextToken());
        
        // 집합 A 입력 받기
        int[] A = new int[nA];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < nA; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        
        // 집합 B 입력 받기
        int[] B = new int[nB];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < nB; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }
        
        // 결과가 증가하는 순서로 출력되어야 하므로, A도 정렬해두자.
        Arrays.sort(A);
        // 이분 탐색을 위해 집합 B를 정렬한다.
        Arrays.sort(B);
        
        // 집합 A의 각 원소에 대해, B에 존재하지 않는다면 결과에 추가
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (int i = 0; i < nA; i++) {
            // 만약 A[i]가 B에 없으면 (binarySearch의 반환값이 음수)
            if (Arrays.binarySearch(B, A[i]) < 0) {
                count++;
                sb.append(A[i]).append(" ");
            }
        }
        
        // 결과 출력
        System.out.println(count);
        if (count > 0) {
            System.out.println(sb.toString().trim());
        }
    }
}
