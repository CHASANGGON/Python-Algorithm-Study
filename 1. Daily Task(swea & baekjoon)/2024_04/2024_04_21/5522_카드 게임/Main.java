import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int total = 0;  // 변수 선언 및 초기화
        for (int i = 1; i <= 5; i++) {
            total += Integer.parseInt(br.readLine()); // 누적합 : 한 줄 입력 받고, 입력 받은 문자열을 정수로 변환
        }
        System.out.print(total);
    }
}