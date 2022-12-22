import java.io.*;
import java.text.DecimalFormat;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        // 소수 4번째 자리까지만 표현하도록 하는 클래스 선언
        DecimalFormat checkFormat = new DecimalFormat("0.####");

        // 친구 수 및 남은 시간 입력
        StringTokenizer bellInfo = new StringTokenizer(input.readLine(), "[ ]");
        int studentNumber = Integer.parseInt(bellInfo.nextToken());
        double timeLeft = Double.parseDouble(bellInfo.nextToken());

        // 학생들의 위치 입력
        long[] studentPosition = new long[studentNumber];

        StringTokenizer positionInfo = new StringTokenizer(input.readLine(), "[ ]");

        for (int i = 0; i < studentNumber; i++) {
            studentPosition[i] = Long.parseLong(positionInfo.nextToken());
        }

        // 학생들의 속력 입력
        long[] studentSpeed = new long[studentNumber];

        StringTokenizer speedInfo = new StringTokenizer(input.readLine(), "[ ]");

        for (int i = 0; i < studentNumber; i++) {
            studentSpeed[i] = Long.parseLong(speedInfo.nextToken());
        }

        // 공통 이동 가능 범위 선언 및 초기값 입력
        double minPosition = Double.parseDouble(checkFormat.format(studentPosition[0] - timeLeft * studentSpeed[0]));
        double maxPosition = Double.parseDouble(checkFormat.format(studentPosition[0] + timeLeft * studentSpeed[0]));

        // 결과 변수 선언
        boolean canMeet = true;

        // 모든 학생들에 대해서 체크
        for (int i = 1; i < studentNumber; i++) {

            // 현재 학생의 이동 범위 연산
            double minNow = Double.parseDouble(checkFormat.format(studentPosition[i] - timeLeft * studentSpeed[i]));
            double maxNow = Double.parseDouble(checkFormat.format(studentPosition[i] + timeLeft * studentSpeed[i]));

            // 만약 공통 이동 가능 범위보다 작다면 갱신
            if (minNow > minPosition) {
                minPosition = minNow;
            }
            if (maxNow < maxPosition) {
                maxPosition = maxNow;
            }

            // 최대값과 최소값이 교차한 경우 이동이 불가능함
            if (minPosition > maxPosition) {
                canMeet = false;
                break;
            }

        }

        // 결과 출력
        if (canMeet) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

    }

}
