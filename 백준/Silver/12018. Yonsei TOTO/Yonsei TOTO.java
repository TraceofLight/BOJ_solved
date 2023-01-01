import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer totoInfo = new StringTokenizer(input.readLine(), "[ ]");

        int subjectNumber = Integer.parseInt(totoInfo.nextToken());
        int totalMileage = Integer.parseInt(totoInfo.nextToken());

        ArrayList<Integer> minMileageList = new ArrayList<>();

        for (int i = 0; i < subjectNumber; i++) {

            StringTokenizer applyInfo = new StringTokenizer(input.readLine(), "[ ]");

            int applyNumber = Integer.parseInt(applyInfo.nextToken());
            int canSubmit = Integer.parseInt(applyInfo.nextToken());

            StringTokenizer mileageInfo = new StringTokenizer(input.readLine(), "[ ]");

            if (applyNumber < canSubmit) {
                minMileageList.add(1);
            } else {

                ArrayList<Integer> mileageList = new ArrayList<>();

                for (int j = 0; j < applyNumber; j++) {
                    mileageList.add(Integer.parseInt(mileageInfo.nextToken()));
                }

                Collections.sort(mileageList, Collections.reverseOrder());

                minMileageList.add(mileageList.get(canSubmit - 1));

            }

        }

        Collections.sort(minMileageList);

        int result = 0;

        for (int i = 0; i < subjectNumber; i++) {

            int nowNeedMileage = minMileageList.get(i);

            if (totalMileage >= nowNeedMileage) {
                totalMileage -= nowNeedMileage;
                result += 1;

            } else {
                break;
            }

        }

        output.write(Integer.toString(result));

        output.flush();
        output.close();

    }

}
