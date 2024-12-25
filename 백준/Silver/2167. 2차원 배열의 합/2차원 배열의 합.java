import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);
        int[][] arr = new int[N][M];

        for (int i = 0; i < N; i++) {
            String[] inputs = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(inputs[j]);
            }
        }

        int K = Integer.parseInt(br.readLine());

        for (int k = 0; k < K; k++) {
            String[] IJXY = br.readLine().split(" ");
            int I = Integer.parseInt(IJXY[0]);
            int J = Integer.parseInt(IJXY[1]);
            int X = Integer.parseInt(IJXY[2]);
            int Y = Integer.parseInt(IJXY[3]);
            int ans = 0;
            for (int i = I - 1; i <= X - 1; i++) {
                for (int j = J - 1; j <= Y - 1; j++) {
                    ans += arr[i][j];
                }
            }
            System.out.println(ans);
        }
    }
}