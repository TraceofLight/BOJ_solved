import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {

            double inputWeight = Double.parseDouble(input.readLine());

            if (inputWeight < 0) {
                break;

            } else {
                double resultWeight = inputWeight * 0.167;
                output.write("Objects weighing " + String.format("%.2f", inputWeight) +
                        " on Earth will weigh " + String.format("%.2f", resultWeight)
                        + " on the moon." + "\n");
            }

        }

        output.flush();
        output.close();

    }

}
