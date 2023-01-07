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

        ArrayList<Integer> lisArr = new ArrayList<>();
        int nowLength = 0;

        for (int i = 0; i < arrLength; i++) {

            int findResult = Collections.binarySearch(lisArr, inputArr[i]);

            if (findResult < 0) {
                findResult = -findResult - 1;
            }


            if (findResult >= nowLength) {
                lisArr.add(inputArr[i]);
                nowLength += 1;

            } else {
                lisArr.set(findResult, inputArr[i]);
            }

        }

        output.write(Integer.toString(nowLength));

        output.flush();
        output.close();

    }

}
