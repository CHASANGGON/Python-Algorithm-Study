import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력을 받기 위한 객체 생성
        
        String[] str = br.readLine().split(" ");
        
        int A = Integer.parseInt(str[0]); // 토큰을 하나씩 넘겨주면서 정수로 변환
        int B = Integer.parseInt(str[1]);

        if(A > B) System.out.println(">");
        else if(A < B) System.out.println("<");
        else System.out.println("==");
    }    
}