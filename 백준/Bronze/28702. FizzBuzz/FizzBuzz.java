import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] input = new String[3];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 3; i++) {
            input[i] = br.readLine();
        }

        int start = -1;

        // 숫자가 포함된 줄이 있으면 그 인덱스를 기반으로 i 추정
        for (int i = 0; i < 3; i++) {
            if (isNumber(input[i])) {
                int num = Integer.parseInt(input[i]);
                start = num - i;
                break;
            }
        }

        // 시작 인덱스 기반으로 다음 출력
        System.out.println(fizzBuzz(start + 3));
    }

    static boolean isNumber(String s) {
        // 숫자인지 확인
        for (int i = 0; i < s.length(); i++) {
            if (!Character.isDigit(s.charAt(i))) return false;
        }
        return true;
    }

    static String fizzBuzz(int i) {
        if (i % 3 == 0 && i % 5 == 0) return "FizzBuzz";
        else if (i % 3 == 0) return "Fizz";
        else if (i % 5 == 0) return "Buzz";
        else return Integer.toString(i);
    }
}
