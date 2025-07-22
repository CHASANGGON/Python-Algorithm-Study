class Solution {
    public int solution(int a, int b) {
        int answer = a * (int)Math.pow(10, String.valueOf(b).length()) + b;
        if (answer < b * (int)Math.pow(10, String.valueOf(a).length()) + a) {
            answer = b * (int)Math.pow(10, String.valueOf(a).length()) + a;
        }
        
        return answer;
    }
}