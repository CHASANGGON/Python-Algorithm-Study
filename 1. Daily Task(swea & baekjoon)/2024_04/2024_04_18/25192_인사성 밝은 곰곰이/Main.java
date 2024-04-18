import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException { // 예외 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력으로부터 숫자 N을 읽어들임
        int N = Integer.parseInt(br.readLine());

        // 정답을 저장할 변수 ans 선언 및 초기화
        int ans = 0;
        
        // 중복된 문자열을 제거하기 위해 HashSet 사용
        HashSet<String> set = new HashSet<>();

        // N만큼 반복하면서 입력 처리
        while(N --> 0) {
            // 한 줄을 읽어들임
            String input = br.readLine();

            // 입력이 "ENTER"인 경우
            if (input.equals("ENTER")) {
                // HashSet에 저장된 문자열의 개수를 ans에 더함
                ans += set.size();
                // HashSet을 비워서 다음 "ENTER" 이전의 문자열들을 처리하기 위해 준비
                set.clear();
                // 다음 반복으로 넘어감
                continue;
            }

            // "ENTER"이 아닌 경우 HashSet에 문자열을 추가
            set.add(input);
        }

        // 정답 출력
        System.out.print(ans + set.size());
    }
}
