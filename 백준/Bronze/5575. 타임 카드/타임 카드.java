import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i = 0; i < 3; i++) {

            StringTokenizer workTime = new StringTokenizer(input.readLine(), "[ ]");

            int startHour = Integer.parseInt(workTime.nextToken());
            int startMin = Integer.parseInt(workTime.nextToken());
            int startSec = Integer.parseInt(workTime.nextToken());
            int endHour = Integer.parseInt(workTime.nextToken());
            int endMin = Integer.parseInt(workTime.nextToken());
            int endSec = Integer.parseInt(workTime.nextToken());

            int resultTime = 3600 * (endHour - startHour) + 60 * (endMin - startMin) + (endSec - startSec);
            int resultHour = resultTime / 3600;
            resultTime %= 3600;
            int resultMin = resultTime / 60;
            resultTime %= 60;
            int resultSec = resultTime;

            output.write(resultHour + " " + resultMin + " " + resultSec + "\n");

        }

        output.flush();
        output.close();

    }

}
