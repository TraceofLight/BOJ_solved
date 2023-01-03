import java.io.*;
import java.util.*;

public class Main {

    public static ArrayList<Integer> resultArr = new ArrayList<>();

    public static void findMinMax(int[] numberArr, int[] operatorArr, int nowResult, int nowIdx, int targetIdx) {

        if (nowIdx == targetIdx) {

            resultArr.add(nowResult);

        } else {

            for (int i = 0; i < 4; i++) {

                if (operatorArr[i] > 0) {

                    operatorArr[i] -= 1;

                    if (i == 0) {
                        findMinMax(numberArr, operatorArr, nowResult + numberArr[nowIdx + 1], nowIdx + 1, targetIdx);
                    } else if (i == 1) {
                        findMinMax(numberArr, operatorArr, nowResult - numberArr[nowIdx + 1], nowIdx + 1, targetIdx);
                    } else if (i == 2) {
                        findMinMax(numberArr, operatorArr, nowResult * numberArr[nowIdx + 1], nowIdx + 1, targetIdx);
                    } else {

                        if (nowResult > 0) {
                            findMinMax(numberArr, operatorArr, (int)(nowResult / numberArr[nowIdx + 1]), nowIdx + 1, targetIdx);
                        } else {
                            findMinMax(numberArr, operatorArr, -((int)(-nowResult / numberArr[nowIdx + 1])), nowIdx + 1, targetIdx);
                        }

                    }

                    operatorArr[i] += 1;

                }

            }

        }

    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int numberAmount = Integer.parseInt(input.readLine());
        int[] numberInfo = new int[numberAmount];
        int[] operatorInfo = new int[4];

        StringTokenizer numbers = new StringTokenizer(input.readLine(), "[ ]");
        for (int i = 0; i < numberAmount; i++) {
            numberInfo[i] = Integer.parseInt(numbers.nextToken());
        }

        StringTokenizer operators = new StringTokenizer(input.readLine(), "[ ]");
        for (int i = 0; i < 4; i++) {
            operatorInfo[i] = Integer.parseInt(operators.nextToken());
        }

        findMinMax(numberInfo, operatorInfo, numberInfo[0], 0, numberAmount - 1);

        int maxVal = Collections.max(resultArr);
        int minVal = Collections.min(resultArr);

        output.write(maxVal + "\n");
        output.write(Integer.toString(minVal));

        output.flush();
        output.close();

    }

}