import java.util.*;

public class Main {
    public static Integer leftMinNumber(String[] targetArr, int arrLength) {

        // 학생 번호의 길이 확인
        int numberLength = targetArr[0].length();

        for (int idx = numberLength - 1; idx >= 0; idx -= 1) {

            // 줄어든 학생 번호를 담을 집합 선언
            Set<String> idSet = new HashSet<>();

            // 집합에 모든 줄어든 학생 번호를 추가
            for (int i = 0; i < arrLength; i += 1) {
                idSet.add(targetArr[i].substring(idx, numberLength));
            }

            // 중복 없이 카운팅한 값이 기존 학생 번호의 갯수랑 동일하다면 전부 구별 가능함
            if (idSet.size() == arrLength) {
                return (numberLength - idx);
            }

        }

        // 줄여서 구분이 불가능했다면 0을 반환
        return 0;

    }

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // 학생 숫자 입력
        int studentNumber = input.nextInt();
        // 학생 번호를 담을 배열 선언
        String[] studentId = new String[studentNumber];

        input.nextLine();

        // 배열에 학생 번호를 추가
        for (int idx = 0; idx < studentNumber; idx += 1) {
            studentId[idx] = input.nextLine();
        }

        // 함수를 호출하여 결과 출력
        System.out.println(leftMinNumber(studentId, studentNumber));

    }
}