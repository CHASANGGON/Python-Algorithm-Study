import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 숫자 입력받기
        String line = br.readLine();
        int[] input = new int[N];
        for (int i = 0; i < N; i++) input[i] = line.charAt(i) - '0';

        // 로직
        Stack<Integer> stack = new Stack<>();
        for (int i : input) {
            // 앞에서부터 현재까지 살펴본 숫자들 중에서
            // 제일 큰 숫자들로 결정하면 됨

            // stack.peek()를 계속 확인하며 앞에서부터 큰 자리를 결정
            // (제일 클지는 보장 못함 -> 나중에 제거될 수도 있기에)
            // 하지만 K가 아직 남아 있다면, 이미 결정돼 있던 수를 제거함
            while (!stack.isEmpty() && K > 0 && stack.peek() < i) {
                stack.pop();
                K--;
            }

            stack.push(i); // 제거했든 안 했든 현재수 추가
//            System.out.println(stack);
        }

        // K가 아직 덜 제거 됨
        // 10 4
        // 4177252841 -> 1
//        System.out.println(K);

        // 남아있는 k만큼 제거
        while (K-- > 0) {
//            System.out.println();
//            System.out.println(stack);
            stack.pop();
        }

        // 출력
        StringBuilder sb = new StringBuilder();
        for (int s : stack) { // 앞에서부터 입력
            sb.append(s);
        }
        System.out.println(sb.toString());
    }
}