import java.io.*;
        import java.util.*;
        import java.util.regex.Pattern;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 전파 기록 갯수 입력
        int radioNumber = Integer.parseInt(input.readLine());

        // 출력 리스트 및 패턴 입력
        ArrayList<String> outputList = new ArrayList<>();
        String pattern = "(100+1+|01)+";

        // 패턴 조건을 확인하고 그에 따른 결과 출력 리스트에 추가
        for (int i = 0; i < radioNumber; i++) {

            String targetString = input.readLine();
            boolean isVerified = Pattern.matches(pattern, targetString);

            if (isVerified) {
                outputList.add("YES");
            } else {
                outputList.add("NO");
            }

        }

        // 출력
        for (int i = 0; i < radioNumber; i++) {
            if (i != radioNumber - 1) {
                output.write(outputList.get(i) + "\n");
            } else {
                output.write(outputList.get(i));
            }
        }

        output.flush();
        output.close();
    }

}
