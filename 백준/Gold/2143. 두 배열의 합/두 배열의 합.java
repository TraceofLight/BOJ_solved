import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int targetValue = Integer.parseInt(input.readLine());

        int arr1Length = Integer.parseInt(input.readLine());
        int[] arr1 = new int[arr1Length + 1];

        StringTokenizer arr1Elements = new StringTokenizer(input.readLine(), "[ ]");

        for (int i = 1; i < arr1Length + 1; i++) {
            arr1[i] = arr1[i - 1] + Integer.parseInt(arr1Elements.nextToken());
        }

        ArrayList<Integer> sumList1 = new ArrayList<>();

        for (int i = 0; i < arr1Length + 1; i++) {
            for (int j = 0; j < i; j++) {
                sumList1.add(arr1[i] - arr1[j]);
            }
        }

        HashMap<Integer, Integer> countInfo = new HashMap<>();

        for (int nowSum : sumList1) {

            countInfo.putIfAbsent(nowSum, 0);
            countInfo.put(nowSum, countInfo.get(nowSum) + 1);

        }

        int arr2Length = Integer.parseInt(input.readLine());
        int[] arr2 = new int[arr2Length + 1];

        StringTokenizer arr2Elements = new StringTokenizer(input.readLine(), "[ ]");

        for (int i = 1; i < arr2Length + 1; i++) {
            arr2[i] = arr2[i - 1] + Integer.parseInt(arr2Elements.nextToken());
        }

        ArrayList<Integer> sumList2 = new ArrayList<>();

        for (int i = 0; i < arr2Length + 1; i++) {
            for (int j = 0; j < i; j++) {
                sumList2.add(arr2[i] - arr2[j]);
            }
        }

        long result = 0;

        for (int eachSum : sumList2) {

            if (countInfo.get(targetValue - eachSum) != null) {
                result += countInfo.get(targetValue - eachSum);
            }

        }

        output.write(Long.toString(result));

        output.flush();
        output.close();

    }

}
