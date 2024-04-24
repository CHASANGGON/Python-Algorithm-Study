import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()); // 한 줄 입력받은 후 추후에 자르기 위해 StringTokenizer에 저장
        int[] arr = new int[3]; // 배열 3칸 선언
        for (int i = 0; i < 3; i++){ // 하나씩 대입
            arr[i] = Integer.parseInt(st.nextToken()); // 토큰화해서
        }
        Arrays.sort(arr); // arr 배열 정렬하기
        for(int i = 0; i < 3; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}