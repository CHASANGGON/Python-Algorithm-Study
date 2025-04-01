import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 입력 받기
        int N = Integer.parseInt(br.readLine());

        // 신청자 수 입력 받기
        int[] applicant = new int[6];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 6; i++) {
            applicant[i] = Integer.parseInt(st.nextToken());
        }

        // 묶음 수 입력 받기
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        // 티셔츠 출력
        int tAns = 0, pAns = 0;
        for (int i = 0; i < 6; i++) {
            pAns += applicant[i];
            tAns += applicant[i] / T;
            if (applicant[i] % T != 0) tAns++;
        }
        System.out.println(tAns);

        // 볼펜수 출력
        System.out.println(pAns / P + " " + pAns % P);
    }
}
