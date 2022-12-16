import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        // 전체 돌의 갯수 입력
        long totalRocks = Long.parseLong(input.readLine());

        // 5의 배수를 유지하면 승리, 완급 조절이 항상 가능
        if (totalRocks % 5 == 2 || totalRocks % 5 == 0) {
            System.out.println("CY");
        } else {
            System.out.println("SK");
        }

    }
}