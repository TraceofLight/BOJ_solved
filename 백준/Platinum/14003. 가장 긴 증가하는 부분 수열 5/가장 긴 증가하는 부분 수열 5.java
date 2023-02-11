import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int arrLength = Integer.parseInt(input.readLine());
        int[] inputArr = new int[arrLength];

        StringTokenizer arrInfo = new StringTokenizer(input.readLine(), "[ ]");
        for (int i = 0; i < arrLength; i++) {
            inputArr[i] = Integer.parseInt(arrInfo.nextToken());
        }

        ArrayList<Integer> LISArr = new ArrayList<>();
        ArrayList<Integer> traceIndexArr = new ArrayList<>();

        int nowLength = 0;

        for (int i = 0; i < arrLength; i++) {

            int findResult = Collections.binarySearch(LISArr, inputArr[i]);
            if (findResult < 0) {
                findResult = -findResult - 1;
            }


            if (findResult >= nowLength) {
                LISArr.add(inputArr[i]);
                traceIndexArr.add(nowLength);
                nowLength += 1;

            } else {
                LISArr.set(findResult, inputArr[i]);
                traceIndexArr.add(findResult);
            }

        }

        Stack<Integer> resultStack = new Stack<>();
        int nowTarget = nowLength - 1;
        int nowIndex = arrLength - 1;

        while (nowTarget >= 0) {
            if (traceIndexArr.get(nowIndex) == nowTarget) {
                resultStack.push(inputArr[nowIndex]);
                nowTarget -= 1;
            }
            nowIndex -= 1;
        }

        output.write(Integer.toString(nowLength) + "\n");

        while (!resultStack.isEmpty()) {
            output.write(Integer.toString(resultStack.pop()));

            if (!resultStack.isEmpty()) {
                output.write(" ");
            }

        }

        output.flush();
        output.close();

    }

}
