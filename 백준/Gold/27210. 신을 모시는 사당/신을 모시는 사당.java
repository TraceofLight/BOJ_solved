import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int statueNumber = Integer.parseInt(input.readLine());

        StringTokenizer statueInfo = new StringTokenizer(input.readLine(), "[ ]");

        int leftValue = 0;
        int rightValue = 0;
        int maxValue = 0;

        for (int i = 0; i < statueNumber; i++) {

            int nowStatue = Integer.parseInt(statueInfo.nextToken());

            if (nowStatue == 1) {
                leftValue += 1;
                rightValue -= 1;

            } else {
                leftValue -= 1;
                rightValue += 1;
            }

            maxValue = Math.max(Math.max(leftValue, rightValue), maxValue);

            rightValue = Math.max(0, rightValue);
            leftValue = Math.max(0, leftValue);

        }

        output.write(Integer.toString(maxValue));

        output.flush();
        output.close();

    }

}
