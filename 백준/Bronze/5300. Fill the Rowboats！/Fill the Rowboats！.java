import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int piratesAmount = Integer.parseInt(input.readLine());

        for (int i = 1; i < piratesAmount + 1; i++) {

            output.write(i + " ");

            if (i % 6 == 0 || i == piratesAmount) {
                output.write("Go!");

                if (i % 6 == 0) {
                    output.write(" ");
                }

            }

        }

        output.flush();
        output.close();

    }

}
