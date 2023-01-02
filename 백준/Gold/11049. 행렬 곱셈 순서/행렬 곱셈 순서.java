import java.io.*;
import java.util.*;

public class Main {

    public static int findMinCalc(int[][] result, ArrayList<int[]> arrInfo, int start, int end) {

        if (result[start][end] == Integer.MAX_VALUE) {

            if (end - start == 1) {

                int nowResult = arrInfo.get(start)[0] * arrInfo.get(start)[1] * arrInfo.get(end)[1];
                result[start][end] = nowResult;

            } else {

                for (int i = start; i < end; i++) {

                    int nowResult = findMinCalc(result, arrInfo, start, i) + findMinCalc(result, arrInfo, i + 1, end)
                            + arrInfo.get(start)[0] * arrInfo.get(i)[1] * arrInfo.get(end)[1];
                    result[start][end] = Math.min(result[start][end], nowResult);

                }

            }

        }

        return result[start][end];

    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int matrixNumber = Integer.parseInt(input.readLine());
        ArrayList<int[]> matrixInfo = new ArrayList<>();

        for (int i = 0; i < matrixNumber; i++) {

            StringTokenizer nowMatrix = new StringTokenizer(input.readLine(), "[ ]");
            int[] nowMatrixInfo = new int[2];

            for (int j = 0; j < 2; j++) {
                nowMatrixInfo[j] = Integer.parseInt(nowMatrix.nextToken());
            }

            matrixInfo.add(nowMatrixInfo);

        }

        int[][] result = new int[matrixNumber][matrixNumber];

        for (int i = 0; i < matrixNumber; i++) {
            for (int j = i; j < matrixNumber; j++) {

                if (i != j) {
                    result[i][j] = Integer.MAX_VALUE;
                }

            }
        }

        output.write(Integer.toString(findMinCalc(result, matrixInfo, 0, matrixNumber - 1)));

        output.flush();
        output.close();

    }

}
