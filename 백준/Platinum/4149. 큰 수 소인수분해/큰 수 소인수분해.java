import java.util.*;

public class Main {

    // 소인수들을 저장할 리스트 (중복 포함)
    private static List<Long> factors = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        sc.close();

        // 1 이하 입력은 의미 없음
        if (n <= 1) {
            throw new IllegalArgumentException("Input must be greater than 1.");
        }

        // 소인수분해 실행
        factorize(n);

        // 결과 정렬 후 출력
        Collections.sort(factors);
        for (long factor : factors) {
            System.out.println(factor);
        }
    }

    // (a * b) % mod 를 overflow 없이 계산
    // → long 범위 초과 방지용 (모듈러 곱셈)
    private static long multiply(long a, long b, long mod) {
        long result = 0;

        // 이진 분할 방식 (덧셈 기반 곱셈)
        while (b > 0) {
            if ((b & 1) == 1) {
                result = (result + a) % mod;
            }
            b >>= 1;
            a = (a * 2) % mod;
        }
        return result;
    }

    // (a^b) % mod 빠른 거듭제곱
    // → Miller-Rabin에서 사용
    private static long power(long a, long b, long mod) {
        long result = 1;

        while (b > 0) {
            if ((b & 1) == 1) {
                result = multiply(result, a, mod);
            }
            b >>= 1;
            a = multiply(a, a, mod);
        }
        return result;
    }

    // Miller-Rabin 소수 판별
    // → n이 소수인지 빠르게 판단
    private static boolean isPrime(long n) {
        if (n <= 1) return false;

        // deterministic base (long 범위에서 충분)
        long[] bases = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};

        // n-1 = d * 2^s 형태로 분해
        long d = n - 1;
        int s = 0;
        while (d % 2 == 0) {
            d /= 2;
            s++;
        }

        for (long a : bases) {
            if (a == n) return true;
            if (a > n) break;

            // a^d % n
            long x = power(a, d, n);

            // 통과 조건
            if (x == 1 || x == n - 1) continue;

            boolean composite = true;

            // 반복 제곱
            for (int r = 0; r < s; r++) {
                x = multiply(x, x, n);

                if (x == n - 1) {
                    composite = false;
                    break;
                }
            }

            // 합성수 판정
            if (composite) return false;
        }

        return true;
    }

    // 최대공약수 (유클리드)
    private static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    // Pollard’s Rho 기반 소인수분해
    private static void factorize(long n) {

        // 종료 조건
        if (n == 1) return;

        // 짝수 처리
        if (n % 2 == 0) {
            factors.add(2L);
            factorize(n / 2);
            return;
        }

        // 소수면 그대로 추가
        if (isPrime(n)) {
            factors.add(n);
            return;
        }

        // Pollard’s Rho 초기값
        long x = 2, y = 2;
        long c = 1;     // f(x) = x^2 + c
        long g = n;     // gcd 값

        Random rand = new Random();

        // g != 1 이 될 때까지 반복
        do {
            // 실패 (g == n)하면 랜덤 재시도
            if (g == n) {
                x = rand.nextInt((int) Math.min(n - 2, Integer.MAX_VALUE)) + 2;
                y = x;
                c = rand.nextInt(20) + 1;
            }

            // x는 한 번 이동
            x = pollardFunction(x, c, n);

            // y는 두 번 이동 (Floyd cycle detection)
            y = pollardFunction(pollardFunction(y, c, n), c, n);

            // 차이의 gcd로 인수 찾기
            g = gcd(Math.abs(x - y), n);

        } while (g == 1);

        // 찾은 인수로 분할 정복
        factorize(n / g);
        factorize(g);
    }

    // f(x) = x^2 + c (mod n)
    // → pseudo-random sequence 생성
    private static long pollardFunction(long x, long c, long n) {
        return (multiply(x, x, n) + c) % n;
    }
}