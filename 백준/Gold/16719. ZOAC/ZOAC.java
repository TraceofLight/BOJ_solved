import java.io.*;
import java.util.*;

public class Main {

    /**
     * 문자열과 표현 배열, 길이가 주어지면 해당하는 문자열을 반환하는 함수
     */
    public static String makeString(String target, boolean[] availableArr, int length) {

        // 공백 문자열 선언
        String result = "";

        // true 처리된 모든 인덱스에 대해서 문자를 추가
        for (int i = 0; i < length; i++) {

            if (availableArr[i]) {
                result = result + target.charAt(i);
            }

        }

        return result;

    }

    /**
     * 글자수가 동일한 문자열 2개 중 사전순 우위를 판단하는 함수
     */
    public static String checkFirstString(String string1, String string2) {

        for (int i = 0; i < string1.length(); i++) {
            if (string1.charAt(i) < string2.charAt(i)) {
                return string1;
            } else if (string1.charAt(i) > string2.charAt(i)) {
                return string2;
            }
        }

        return string1;

    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 문자열 입력 및 길이 확인
        String inputString = input.readLine();
        int stringLength = inputString.length();

        // 우선순위 큐 선언
        PriorityQueue<Character> charQueue = new PriorityQueue<>();

        // 우선순위 큐에 모든 문자 입력
        for (int i = 0; i < stringLength; i++) {
            charQueue.add(inputString.charAt(i));
        }

        // 우선순위가 돌아왔는지 체크할 배열 선언
        boolean[] nowInArr = new boolean[stringLength];

        // 출력 리스트 선언
        ArrayList<String> printArr = new ArrayList<>();

        // 인덱스 기록 변수 선언
        int memorizeIdx = 0;

        for (int count = 0; count < stringLength; count++) {

            // 우선순위가 돌아온 문자열 확인

            if (count == 0 && !charQueue.isEmpty()) {

                char firstChar = charQueue.poll();

                for (int i = 0; i < stringLength; i++) {

                    if (!nowInArr[i] && inputString.charAt(i) == firstChar) {
                        nowInArr[i] = true;
                        break;
                    }

                }

                printArr.add(makeString(inputString, nowInArr, stringLength));
                continue;

            }

            // 후보가 여럿인 경우 체크를 위한 Flag 선언
            String checkString = "";
            boolean isFirst = true;

            // 사전순 처리
            for (int i = 0; i < stringLength; i++) {

                if (!nowInArr[i]) {

                    // 아직 처리가 한 번도 안된 경우 초기값 설정
                    if (isFirst) {

                        isFirst = false;
                        nowInArr[i] = true;
                        memorizeIdx = i;
                        checkString = makeString(inputString, nowInArr, stringLength);

                        // 그렇지 않을 경우 우위 비교
                    } else {

                        nowInArr[memorizeIdx] = false;
                        nowInArr[i] = true;
                        String nowCheckString = makeString(inputString, nowInArr, stringLength);

                        // 기존값이 여전히 사전순 우위라면 되돌림
                        if (checkFirstString(checkString, nowCheckString).equals(checkString)) {
                            nowInArr[memorizeIdx] = true;
                            nowInArr[i] = false;

                            // 그렇지 않을 경우 기록된 인덱스값과 String 값을 변경
                        } else {
                            checkString = nowCheckString;
                            memorizeIdx = i;
                        }

                    }

                }

            }

            // 값을 출력 리스트에 추가
            printArr.add(makeString(inputString, nowInArr, stringLength));

        }

        // 사전순 출력
        for (int i = 0; i < stringLength; i++) {

            if (i == stringLength - 1 && !printArr.isEmpty()) {
                output.write(printArr.get(i));
            } else {
                output.write(printArr.get(i) + "\n");
            }

        }

        output.flush();
        output.close();

    }

}