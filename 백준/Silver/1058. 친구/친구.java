import java.io.*;
import java.util.*;

public class Main {

    /** 배열의 최댓값을 반환하는 함수 */
    public static int max(ArrayList<Integer> targetArr) {

        int result = -2000000000;

        if (targetArr.isEmpty()) {
            return result;
        }

        for (int i = 0; i < targetArr.size(); i++) {
            if (i == 0) {
                result = targetArr.get(i);
            } else {
                result = Math.max(result, targetArr.get(i));
            }
        }

        return result;

    }

    /** 문자열 자료형을 Integer 자료형으로 변경하는 함수 */
    public static int strToInt(String target) {
        return Integer.parseInt(target);
    }

    public static void main(String[] args) throws IOException {

        // 입출력 변환
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 사람의 숫자 입력
        int personNumber = strToInt(input.readLine());

        // 관계 그래프 2차원 배열 선언 및 공집합으로 초기화
        ArrayList<HashSet<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < personNumber; i++) {
            graph.add(new HashSet<>());
        }

        // 친구 관계 입력
        for (int i = 0; i < personNumber; i++) {

            String friendInfo = input.readLine();

            for (int j = 0; j < personNumber; j++) {

                if (friendInfo.charAt(j) == 'Y') {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }

            }
        }

        // 2-친구값을 담을 배열 선언
        ArrayList<Integer> friend2List = new ArrayList<>();

        // Depth First Search
        Stack<Integer[]> progressStack = new Stack<>();

        for (int eachPerson = 0; eachPerson < personNumber; eachPerson++) {

            boolean[] visited = new boolean[personNumber];
            progressStack.push(new Integer[] {eachPerson, 0});
            int friend2Counter = 0;

            visited[eachPerson] = true;

            while (!progressStack.isEmpty()) {

                Integer[] nowPersonInfo = progressStack.pop();
                int nowPerson = nowPersonInfo[0];
                int connectCounter = nowPersonInfo[1];

                if (connectCounter < 2) {
                    for (int nextPerson : graph.get(nowPerson)) {

                        if (!visited[nextPerson]) {
                            visited[nextPerson] = true;
                            progressStack.push(new Integer[] {nextPerson, connectCounter + 1});
                            friend2Counter += 1;
                        }

                    }
                }

            }

            friend2List.add(friend2Counter);

        }

        // 2-친구값들 중 최댓값을 출력
        output.write(Integer.toString(max(friend2List)));
        output.flush();
        output.close();

    }
}