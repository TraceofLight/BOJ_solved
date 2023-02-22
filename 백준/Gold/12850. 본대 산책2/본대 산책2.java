import java.io.*;
import java.util.*;

public class Main {

    public static HashMap<Integer, int[][]> matrixRecord = new HashMap<>();

    public static int[][] matrixCalculation(int[][] matrix1, int[][] matrix2) {
        /* 행렬 연산 함수 */

        int[][] resultArr = new int[8][8];

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {

                long sum = 0;

                for (int k = 0; k < 8; k++) {
                    sum += ((long) matrix1[i][k] * (long) matrix2[k][j]) % 1000000007;
                }

                resultArr[i][j] = (int) (sum % 1000000007);

            }
        }

        return resultArr;
    }

    public static int[][] matrixDivision(HashMap<Integer, int[][]> matrixInfo, int calculationCount) {
        /* 분할 정복을 통한 행렬 연산 함수 */

        int halfCount = calculationCount / 2;

        int[][] halfMatrix;
        int[][] otherHalfMatrix;

        // 기존 값이 존재할 경우 불러오기
        if (matrixInfo.containsKey(halfCount)) {
            halfMatrix = matrixInfo.get(halfCount);
        } else {
            halfMatrix = matrixDivision(matrixInfo, halfCount);
        }

        if (matrixInfo.containsKey(calculationCount - halfCount)) {
            otherHalfMatrix = matrixInfo.get(calculationCount - halfCount);
        } else {
            otherHalfMatrix = matrixDivision(matrixInfo, calculationCount - halfCount);
        }

        // 연산 후 행렬 반환
        int[][] calculationResult = matrixCalculation(halfMatrix, otherHalfMatrix);
        matrixInfo.putIfAbsent(calculationCount, calculationResult);

        return calculationResult;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int walkTime = Integer.parseInt(input.readLine());

        // 기본 행렬 및 본대 인접 행렬 선언
        int[][] baseMatrix = {
                {1, 0, 0, 0, 0, 0, 0, 0},
                {0, 1, 0, 0, 0, 0, 0, 0},
                {0, 0, 1, 0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0, 0, 0, 0},
                {0, 0, 0, 0, 1, 0, 0, 0},
                {0, 0, 0, 0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0, 0, 1, 0},
                {0, 0, 0, 0, 0, 0, 0, 1},
        };

        int[][] graph = {
                {0, 1, 1, 0, 0, 0, 0, 0},
                {1, 0, 0, 1, 0, 0, 0, 0},
                {1, 0, 0, 1, 1, 0, 0, 0},
                {0, 1, 1, 0, 1, 1, 0, 0},
                {0, 0, 1, 1, 0, 1, 1, 0},
                {0, 0, 0, 1, 1, 0, 1, 1},
                {0, 0, 0, 0, 1, 1, 0, 1},
                {0, 0, 0, 0, 0, 1, 1, 0},
        };

        // 해시맵에 초기값들 등록
        matrixRecord.put(0, baseMatrix);
        matrixRecord.put(1, graph);

        // 함수를 통해 분할정복 연산 실행
        matrixDivision(matrixRecord, walkTime);

        // 결과 출력
        output.write(Integer.toString(matrixRecord.get(walkTime)[7][7]));

        output.flush();
        output.close();

    }

}
