import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // throws IOException 은 BufferedReader을 사용할 때 필수인 듯..!
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int day = Integer.parseInt(br.readLine()); // day 입력
        StringTokenizer nums = new StringTokenizer(br.readLine()); // 차량 번호 1의 자리 입력
        int answer = 0;

        for (int i = 0; i < 5; i++) { // 차량은 총 5대
            // 문자열을 슬라이싱해서 정수형으로 변환해서 day와 비교
            if(day == Integer.parseInt(nums.nextToken())) { 
                answer++; // day와 일치하면 answer +1
            }
        }
        System.out.print(answer);
    }
}
