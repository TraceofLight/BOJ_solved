import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // 낼 수 있는 소리 입력
        String userSound = input.nextLine();
        String doctorSound = input.nextLine();

        // 의사가 요구하는 소리만큼 낼 수 없다면 no 출력
        if (userSound.length() < doctorSound.length()) {
            System.out.println("no");

        // 낼 수 있다면 go 출력
        } else {
            System.out.println("go");
        }

    }
}