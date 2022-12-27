import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        // 문자열 입력
        String inputString = input.readLine();

        // 갯수를 담을 배열 선언
        int[] count = new int[26];

        // 대문자화
        String upperCaseString = inputString.toUpperCase();

        // Counting
        for (int i = 0; i < upperCaseString.length(); i++) {

            int nowChar = upperCaseString.charAt(i);
            count[nowChar - 65] += 1;

        }

        // 최대 카운팅 결과 및 최대값의 갯수 변수 선언
        int maxCount = 0;
        int maxNumbers = 0;
        int result = 0;

        for (int i = 0; i < 26; i++) {

            int nowCount = count[i];

            // 현재 카운팅 갯수보다 크면 갱신
            if (nowCount > maxCount) {
                maxCount = nowCount;
                maxNumbers = 1;
                result = 65 + i;

                // 같으면 갯수 1 카운팅
            } else if (nowCount == maxCount) {
                maxNumbers += 1;
            }
        }

        // 문제 조건에 따라 출력
        if (maxNumbers > 1) {
            System.out.println("?");
        } else {
            System.out.println((char) result);
        }

    }

}