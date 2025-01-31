import java.util.*;

class Solution {
    List<int[]> moves = new ArrayList<>();

    public int[][] solution(int n) {
        hanoi(n, 1, 3, 2);
        return moves.toArray(new int[moves.size()][]); // List -> 2D array 변환
    }

    private void hanoi(int n, int from, int to, int via) {
        if (n == 1) {
            moves.add(new int[]{from, to}); // 기저 조건: 원판 1개를 옮김
            return;
        }
        hanoi(n - 1, from, via, to); // Step 1: n-1개의 원판을 보조 기둥으로 이동
        moves.add(new int[]{from, to});    // Step 2: 가장 큰 원판을 목표 기둥으로 이동
        hanoi(n - 1, via, to, from); // Step 3: 보조 기둥의 n-1개 원판을 목표 기둥으로 이동
    }
}
