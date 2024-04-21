import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int totalScore = 0;

        for (int i = 0; i < 5; i++) {
            int score = Integer.parseInt(br.readLine());
            if (score < 40) {
                score = 40; // 점수가 40점 미만인 경우 40점으로 변환
            }
            totalScore += score;
        }

        System.out.println(totalScore / 5);
    }
}
