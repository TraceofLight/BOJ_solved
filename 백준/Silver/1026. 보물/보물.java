import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int elementNumber = Integer.parseInt(input.readLine());

        StringTokenizer aGroupInfo = new StringTokenizer(input.readLine(), "[ ]");
        ArrayList<Integer> aGroup = new ArrayList<>();

        for (int i = 0; i < elementNumber; i++) {
            aGroup.add(Integer.parseInt(aGroupInfo.nextToken()));
        }

        StringTokenizer bGroupInfo = new StringTokenizer(input.readLine(), "[ ]");
        ArrayList<Integer> bGroup = new ArrayList<>();

        for (int i = 0; i < elementNumber; i++) {
            bGroup.add(Integer.parseInt(bGroupInfo.nextToken()));
        }

        Collections.sort(aGroup);
        bGroup.sort(Comparator.reverseOrder());

        int result = 0;

        for (int i = 0; i < elementNumber; i++) {
            result += aGroup.get(i) * bGroup.get(i);
        }

        output.write(Integer.toString(result));

        output.flush();
        output.close();

    }

}
