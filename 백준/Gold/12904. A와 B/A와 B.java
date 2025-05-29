import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

class Info {
    int len;
    String str;
    boolean fOrB; // true는 정방향, false는 역방향

    Info(int len, String str, boolean fOrB) {
        this.len = len;
        this.str = str;
        this.fOrB = fOrB;
    }
}

public class Main {
    private static String S, T;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        S = br.readLine();
        T = br.readLine();

        // greedy: 역방향으로 접근 - T -> S로
        // A와 B를 추가하는 방법은 한 가지밖에 안 존재함
        // 그렇기에 경로는 한 가지고, 정답도 한 가지만 존재함!
        // 그래서 이 방식으로 풀 수 있는 것
        Info info = new Info(T.length(), T, true); // 정방향이라고 가정
        int len = S.length();

        while (info.len != len) {
            char lastChar;
            if (info.fOrB) {
                lastChar = info.str.charAt(info.len - 1);
            } else {
                lastChar = info.str.charAt(0);
            }


            if (lastChar == 'A') { // A 제거
                // 1. 정방향: 뒤에서 제거
                if (info.fOrB) info.str = info.str.substring(0, info.len - 1);
                    // 1. 역방향: 앞에서 제거
                else info.str = info.str.substring(1, info.len);
            } else {
                // 1. 정방향: 뒤에서 제거
                if (info.fOrB) info.str = info.str.substring(0, info.len - 1);
                    // 1. 역방향: 앞에서 제거
                else info.str = info.str.substring(1, info.len);

                // 2. 방향 전환
                info.fOrB = !info.fOrB;
            }

            info.len--; // 3. 길이 감소
        }

        // 방향 고려
        if (!info.fOrB) {
            StringBuilder sb = new StringBuilder();
            for (int i = info.len - 1; i >= 0; i--) {
                sb.append(info.str.charAt(i));
            }
            info.str = sb.toString();
        }

        // 출력
        if (S.equals(info.str)) System.out.println(1);
        else System.out.println(0);

    }


}