import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        solve();
    }

    private static void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String target = br.readLine();
        int pointer = 0;

        int N = 0;
        while (N++ <= 30000) { // 수는 최대 3000, 0 ~ 9 는 10: 3000 * 10 = 30,000
            String tmp = String.valueOf(N); // 정수 N을 문자열로 변환 -> 문자열이 되고, 인덱스로 접근 가능
            for (int i = 0; i < tmp.length(); i++) {
                if (tmp.charAt(i) == target.charAt(pointer)) pointer++;
                if (pointer == target.length()) {
                    System.out.println(N);
                    return;
                }
            }
        }
    }
}