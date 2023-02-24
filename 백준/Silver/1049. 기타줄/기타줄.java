import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer guitarInfo = new StringTokenizer(input.readLine(), "[ ]");

        int needString = Integer.parseInt(guitarInfo.nextToken());
        int brandNumber = Integer.parseInt(guitarInfo.nextToken());

        ArrayList<Integer> fullPackageArr = new ArrayList<>();
        ArrayList<Integer> singleStringArr = new ArrayList<>();

        for (int i = 0; i < brandNumber; i++) {
            StringTokenizer brandInfo = new StringTokenizer(input.readLine(), "[ ]");
            fullPackageArr.add(Integer.parseInt(brandInfo.nextToken()));
            singleStringArr.add(Integer.parseInt(brandInfo.nextToken()));
        }

        Collections.sort(fullPackageArr);
        Collections.sort(singleStringArr);

        int minFullPackage = fullPackageArr.get(0);
        int minSingleString = singleStringArr.get(0);

        int result = 0;

        while (needString > 0) {

            if (needString > 6) {
                if (minFullPackage < minSingleString * 6) {
                    result += (needString / 6) * minFullPackage;
                    needString %= 6;
                } else {
                    result = needString * minSingleString;
                    needString = 0;
                }
            } else {
                if (minFullPackage < minSingleString * needString) {
                    result += minFullPackage;
                    needString = 0;
                } else {
                    result += needString * minSingleString;
                    needString = 0;
                }
            }

        }

        output.write(Integer.toString(result));

        output.flush();
        output.close();

    }

}
