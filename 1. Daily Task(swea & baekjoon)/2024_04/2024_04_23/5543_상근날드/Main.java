import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int min_burger = 2000;
        int min_drink = 2000;

        for (int i = 0; i < 3; i++) {
            int burger = Integer.parseInt(br.readLine());
            if (min_burger > burger) {
                min_burger = burger;
            }
        }

        for (int i = 0; i < 2; i++) {
            int drink = Integer.parseInt(br.readLine());
            if (min_drink > drink) {
                min_drink = drink;
            }
        }

        System.out.print(min_burger + min_drink - 50);
    }
}