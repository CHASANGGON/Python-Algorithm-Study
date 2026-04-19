import java.io.*;
import java.util.*;

public class Main {

    // 복소수 클래스 (FFT용)
    static class Complex {
        double real, imag;

        Complex(double real, double imag) {
            this.real = real;
            this.imag = imag;
        }

        Complex add(Complex o) {
            return new Complex(real + o.real, imag + o.imag);
        }

        Complex subtract(Complex o) {
            return new Complex(real - o.real, imag - o.imag);
        }

        // 복소수 곱셈
        Complex multiply(Complex o) {
            return new Complex(real * o.real - imag * o.imag,
                               real * o.imag + imag * o.real);
        }

        // 역 FFT에서 나누기용
        Complex divide(double val) {
            return new Complex(real / val, imag / val);
        }
    }

    // FFT / 역 FFT
    static void fft(Complex[] a, boolean invert) {
        int n = a.length;

        // bit reversal (인덱스 재배열)
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            while (j >= bit) {
                j -= bit;
                bit >>= 1;
            }
            j += bit;

            if (i < j) {
                Complex temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }

        // FFT 핵심 로직 (divide & conquer)
        for (int len = 2; len <= n; len <<= 1) {
            double angle = 2 * Math.PI / len * (invert ? -1 : 1);
            Complex wlen = new Complex(Math.cos(angle), Math.sin(angle));

            for (int i = 0; i < n; i += len) {
                Complex w = new Complex(1, 0);

                for (int j = 0; j < len / 2; j++) {
                    Complex u = a[i + j];
                    Complex v = a[i + j + len / 2].multiply(w);

                    a[i + j] = u.add(v);
                    a[i + j + len / 2] = u.subtract(v);

                    w = w.multiply(wlen);
                }
            }
        }

        // 역 FFT면 n으로 나눠줘야 함
        if (invert) {
            for (int i = 0; i < n; i++) {
                a[i] = a[i].divide(n);
            }
        }
    }

    // convolution (다항식 곱)
    static long[] multiply(long[] a, long[] b) {
        int n = 1;
        // 결과 길이 맞추기 (2의 거듭제곱)
        while (n < a.length + b.length) n <<= 1;

        Complex[] fa = new Complex[n];
        Complex[] fb = new Complex[n];

        // 배열을 복소수 배열로 변환
        for (int i = 0; i < n; i++) {
            fa[i] = new Complex(i < a.length ? a[i] : 0, 0);
            fb[i] = new Complex(i < b.length ? b[i] : 0, 0);
        }

        // 각각 FFT
        fft(fa, false);
        fft(fb, false);

        // 점별 곱 (핵심: convolution = 주파수 영역 곱)
        for (int i = 0; i < n; i++) {
            fa[i] = fa[i].multiply(fb[i]);
        }

        // 역 FFT → 실제 convolution 결과
        fft(fa, true);

        // 실수부만 반올림해서 결과로 사용
        long[] result = new long[n];
        for (int i = 0; i < n; i++) {
            result[i] = Math.round(fa[i].real);
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // X를 2배로 만들어서 "회전"을 선형 배열에서 처리
        long[] x = new long[n * 2];
        long[] y = new long[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            x[i] = Long.parseLong(st.nextToken());
            x[i + n] = x[i]; // X 이어붙이기 (circular → linear)
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            // Y를 뒤집어서 convolution 형태로 맞춤
            y[n - i - 1] = Long.parseLong(st.nextToken());
        }

        // convolution 수행
        long[] result = multiply(x, y);

        // 결과 중에서 "유효한 회전 구간"만 확인
        // (n-1 ~ 2n-2 구간이 각각 k=0~n-1 회전에 대응)
        long maxScore = 0;
        for (int i = n - 1; i < n + n - 1; i++) {
            maxScore = Math.max(maxScore, result[i]);
        }

        System.out.println(maxScore);
    }
}