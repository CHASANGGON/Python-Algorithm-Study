import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        final int r = 31;
        final int M = 1234567891;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine()); // 문자열 길이
        String str = br.readLine(); // 문자열 입력

        long hash = 0;
        long power = 1;

        for (int i = 0; i < L; i++) {
            int value = str.charAt(i) - 'a' + 1; // a=1, ..., z=26
            hash = (hash + value * power) % M;
            power = (power * r) % M;
        }

        System.out.println(hash);
    }
}
