import java.io.*;

public class Main {

    public static int strToInt(String target) {
        return Integer.parseInt(target);
    }

    public static void main(String[] args) throws IOException{

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 표의 너비 및 탐색할 숫자 입력
        int cycleWidth = strToInt(input.readLine());
        int targetNumber = strToInt(input.readLine());

        // 표의 정보를 담을 2차원 배열 선언
        int[][] cycleArr = new int[cycleWidth][cycleWidth];

        // 중간 좌표 및 탐색 결과 변수 선언
        int middle = cycleWidth / 2;
        int resultY = 0;
        int resultX = 0;

        // y = x 위의 점 정보 우선 기록
        for (int i = 0; i < cycleWidth; i++) {

            if (i <= middle) {
                cycleArr[i][i] = (int)(Math.pow(2 * (middle - i) + 1, 2));
            } else {
                cycleArr[i][i] = (int)(Math.pow(2 * (middle - i) + 1, 2)) - 4 * (middle - i);
            }

        }

        // 나머지 좌표 정보 기록
        for (int yIdx = 0; yIdx < cycleWidth; yIdx++) {
            for (int xIdx = 0; xIdx < cycleWidth; xIdx++) {

                int distY = Math.abs(yIdx - middle);
                int distX = Math.abs(xIdx - middle);

                if (distY >= distX) {

                    if (yIdx > xIdx) {

                        cycleArr[yIdx][xIdx] = (
                                cycleArr[middle - distY][middle - distY]
                                        - Math.abs(middle - distY - yIdx)
                                        - Math.abs(middle - distY - xIdx)
                        );

                    } else if (yIdx < xIdx) {

                        cycleArr[yIdx][xIdx] = (
                                cycleArr[middle + distY][middle + distY]
                                        - Math.abs(middle + distY - yIdx)
                                        - Math.abs(middle + distY - xIdx)
                        );

                    }

                } else {

                    if (yIdx > xIdx) {

                        cycleArr[yIdx][xIdx] = (
                                cycleArr[middle - distX][middle - distX]
                                        - Math.abs(middle - distX - yIdx)
                                        - Math.abs(middle - distX - xIdx)
                        );

                    } else if (yIdx < xIdx) {

                        cycleArr[yIdx][xIdx] = (
                                cycleArr[middle + distX][middle + distX]
                                        - Math.abs(middle + distX - yIdx)
                                        - Math.abs(middle + distX - xIdx)
                        );

                    }

                }

                if (cycleArr[yIdx][xIdx] == targetNumber) {
                    resultY = yIdx + 1;
                    resultX = xIdx + 1;
                }

            }

        }

        // 문제 요구 조건에 맞춰 출력
        for (int i = 0; i < cycleWidth; i++) {
            for (int j = 0; j < cycleWidth; j++) {

                if (j == cycleWidth - 1) {
                    output.write(cycleArr[i][j] + "\n");
                } else {
                    output.write(cycleArr[i][j] + " ");
                }

            }
        }

        output.write(resultY + " " + resultX);
        output.flush();
        output.close();

    }
}