import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        char temp; // 어차피 값을 대입할 것이기 때문에 초기화 안 해도 됨
        Scanner sc = new Scanner(System.in); // 입력 받기 위한 Scanner 객체 생성
        String input = sc.nextLine(); // 한 줄 입력 받기
        String output = ""; // output 변수 초기화

        for(int i =0; i < input.length(); i++){ // 입력의 길이만큼 반복
            
            temp = input.charAt(i); // c나 파이썬에서는 input[i]로 인덱스로 접근 가능하지만 자바는 안 됨

            // 상식처럼 알아둬야 할 것
            // 대문자 A의 아스키 코드는 65
            // 소문자 a의 아스키 코드는 97
            // 따라서 아스키 코드값을 이용해서 대소문자를 판단
            // 파이썬에서는 char 또는 ord 를 통해서 문자와 아스키코드의 변환을 했지만
            // 자바에서는 그냥 바로 비교하면 알아서 아스키 코드값으로 판단한다.
            if((65 <= temp) && (temp <=90)) { 
                output += Character.toLowerCase(temp); // 대문자를 소문자로 변경하여 추가
            }
            else if((97 <= temp) && (temp <= 122)) {
                output += Character.toUpperCase(temp); // 소문자를 대문자로 변경하여 추가
            } else {
                output += temp; // 알파벳이 아닌 경우 그대로 추가
            }
        }
        System.out.println(output); // 줄바꿈(개행)을 포함한 한 줄로 출력
    }
}