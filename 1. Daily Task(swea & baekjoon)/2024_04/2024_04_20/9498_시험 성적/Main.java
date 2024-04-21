import java.io.IOException;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws IOException{ // 아직까지 왜 쓰는지 잘 모름
        
        Scanner sc = new Scanner(System.in); // 느리지만 입력을 받는 간단한 방법 - 파이썬의 기본 input 같은 느낌?

        // Scanner를 통해서 입력을 받는 여러 방법이 있는데 
        // 그 중에서 정수를 입력 받는 방법
        int score = sc.nextInt(); // 입력을 받으려면 먼저 자료형을 명시해서 변수 선언을 해야한다

        if (score <= 100 && score >= 90){ // AND와 <=를 보면 파이썬은 참 쉽고 편리한 언어이다..! 
            System.out.println("A"); // 줄바꿈을 하면서 출력하는 방법
        }
        // elif 는 c 자바 파이썬 중에 파이썬만 있네
        else if(score <= 89 && score >= 80){
            System.out.printf("B");
        }
        else if(score <= 79 && score >= 70) System.out.print("C"); // 실행문이 한 줄이면 괄호로 안 감싸도 됨
        else if(score <= 69 && score >= 60) System.out.print("D");
        else System.out.println("F");
    }
    
}