import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        // 입력을 받기 위한 BufferReader 객체 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 사람 수 입력 받기
        int N = Integer.parseInt(br.readLine());

        // 중복을 허용하지 않는 Set 생성
        Set<String> set = new HashSet<>();

        // 총총이는 어차피 추가해야하기에 미리 추가
        set.add("ChongChong");

        // 한 줄을 공백을 기준으로 나누기 위한 StringTokenizer 객체 생성
        StringTokenizer st;

        // N번 반복하여 입력 받음
        for (int i = 0; i < N; i++) {
            // 한 줄을 공백을 기준으로 나누기 위한 StringTokenizer 객체 생성
            st = new StringTokenizer(br.readLine());

            // 입력
            String person1 = st.nextToken();
            String person2 = st.nextToken();
            if (set.contains(person1) || set.contains(person2)) { // 둘 중 한 명이라도 해쉬셋에 있으면
                set.add(person1); // 둘 다 추가
                set.add(person2); // 둘 다 추가
            }
        }
        System.out.println(set.size());
    }
}