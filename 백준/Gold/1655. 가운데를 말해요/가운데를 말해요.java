import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 외치는 정수의 갯수 입력
        int arrNumber = Integer.parseInt(input.readLine());

        // 정순 우선순위큐와 역순 우선순위큐를 하나씩 선언
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        PriorityQueue<Integer> reversedPriorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        ArrayList<Integer> resultArr = new ArrayList<>();

        for (int i = 0; i < arrNumber; i++) {

            // 숫자 반복 입력
            int nowNumber = Integer.parseInt(input.readLine());

            // 첫 번째 원소인 경우 그대로 출력 리스트에 추가
            if (i == 0) {
                reversedPriorityQueue.add(nowNumber);
                resultArr.add(nowNumber);

            } else {

                // 홀수 번째의 경우 역순 우선순위큐에 추가
                if (i % 2 == 0) {
                    reversedPriorityQueue.add(nowNumber);

                    // 짝수 번째의 경우 정순 우선순위큐에 추가
                } else {
                    priorityQueue.add(nowNumber);
                }

                // 크기 역전 보정
                while (reversedPriorityQueue.peek() > priorityQueue.peek()) {

                    int temp1 = reversedPriorityQueue.poll();
                    int temp2 = priorityQueue.poll();

                    priorityQueue.add(temp1);
                    reversedPriorityQueue.add(temp2);

                }

                // 중앙값 출력 리스트에 추가
                resultArr.add(reversedPriorityQueue.peek());

            }

        }

        // 문제 조건에 맞춰 출력
        for (int i = 0; i < arrNumber; i++) {

            if (i != arrNumber - 1) {
                output.write(resultArr.get(i).toString() + "\n");
            } else {
                output.write(resultArr.get(i).toString());
            }

        }

        output.flush();
        output.close();

    }

}