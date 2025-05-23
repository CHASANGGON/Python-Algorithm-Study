import java.io.*;
import java.util.*;

public class Main {
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        // pq 생성
        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> big = new PriorityQueue<>();

        while (N-- > 0) {
            small.add(Integer.parseInt(br.readLine()));

            if (!big.isEmpty() && small.peek() > big.peek()) {
                small.add(big.poll());
                big.add(small.poll());
            }

            if (small.size() > big.size() + 1) {
                big.add(small.poll());
            }

            sb.append(small.peek()).append("\n");
        }

        System.out.println(sb.toString());
    }
}
