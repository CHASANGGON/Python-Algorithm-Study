import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nums = new StringTokenizer(br.readLine());
        int snack = Integer.parseInt(nums.nextToken());
        int count = Integer.parseInt(nums.nextToken());
        int money = Integer.parseInt(nums.nextToken());
        int ans = 0;
        if(snack*count > money) {
            ans = snack*count - money;
        }
        System.out.println(ans);
    }
}