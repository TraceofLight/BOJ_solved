import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        String memberName;

        while ((memberName = input.readLine()) != null) {

            StringBuilder result = new StringBuilder();

            for (int i = 0; i < memberName.length(); i++) {

                if (memberName.charAt(i) == 'i') {
                    result.append('e');
                } else if (memberName.charAt(i) == 'e') {
                    result.append('i');
                } else if (memberName.charAt(i) == 'I') {
                    result.append('E');
                } else if (memberName.charAt(i) == 'E') {
                    result.append('I');
                } else {
                    result.append(memberName.charAt(i));
                }

            }

            output.write(result + "\n");

        }

        output.flush();
        output.close();

    }

}