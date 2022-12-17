import java.io.*;
import java.util.*;

public class Main {

    // INF 변수 선언
    public static int INF = 2000000000;
    public static int width;

    // 일부 델타 탐색을 위한 배열 선언
    public static int[] directionY = new int[]{0, 1};
    public static int[] directionX = new int[]{1, 0};

    /**
     * 노드 클래스 정의
     */
    public static class Node implements Comparable<Node> {
        int[] idx;
        int cost;

        Node(int[] idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node node) {
            return this.cost - node.cost;
        }

    }

    /**
     * str -> int 형변환 함수
     */
    public static int strToInt(String target) {
        return Integer.parseInt(target);
    }

    /**
     * 목적지까지의 최소비용을 확인하는 함수
     */
    public static int findMinCost(ArrayList<Integer>[] targetArr) {

        // Dijkstra Algorithm

        // 우선순위큐 선언
        PriorityQueue<Node> progressQue = new PriorityQueue<>();

        // 각 좌표에 닿을 수 있는 최소비용을 담은 2차원 배열 선언
        int[][] costArr = new int[width][width];
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < width; j++) {
                costArr[i][j] = INF;
            }
        }

        costArr[0][0] = 0;

        Node initialNode = new Node(new int[]{0, 0}, 0);
        progressQue.add(initialNode);

        while (!progressQue.isEmpty()) {

            Node nowNode = progressQue.poll();
            int nowY = nowNode.idx[0];
            int nowX = nowNode.idx[1];
            int nowCost = nowNode.cost;

            if (nowCost <= costArr[nowY][nowX]) {

                for (int i = 0; i < 2; i++) {

                    int nextY = nowY + directionY[i];
                    int nextX = nowX + directionX[i];
                    int nextCost;

                    // 배열 범위를 넘지 않는 상태에서 조사
                    if (0 <= nextX && nextX < width && 0 <= nextY && nextY < width) {

                        // 다음 지점값보다 현재 지점값이 같거나 작은 경우
                        if (targetArr[nextY].get(nextX) >= targetArr[nowY].get(nowX)) {

                            // 추가될 비용 변수 선언
                            int addCost = targetArr[nextY].get(nextX) - targetArr[nowY].get(nowX) + 1;

                            // 추가 비용을 합산한 값으로 다음 지점까지의 비용 갱신
                            nextCost = nowCost + addCost;

                            // 다음 지점값보다 현재 지점값이 큰 경우 비용은 그대로
                        } else {
                            nextCost = nowCost;
                        }

                        // 다음 지점에서의 최소 비용보다 현재 지점에서 다음 지점까지 갈 때의 최소 비용이 작다면 갱신 후 우선순위 큐에 추가
                        if (costArr[nextY][nextX] > nextCost) {

                            costArr[nextY][nextX] = nextCost;
                            progressQue.add(new Node(new int[]{nextY, nextX}, nextCost));

                        }

                    }

                }

            }

        }

        // 최종적으로 목적지의 갱신된 최소값을 반환
        return costArr[width - 1][width - 1];

    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 배열의 길이 입력
        width = strToInt(input.readLine());

        // 2차원 배열 선언
        ArrayList<Integer>[] arrInfo = new ArrayList[width];

        // 배열값 정보 입력
        for (int yIdx = 0; yIdx < width; yIdx++) {

            arrInfo[yIdx] = new ArrayList<>();
            StringTokenizer arrLine = new StringTokenizer(input.readLine(), "[ ]");

            while (arrLine.hasMoreTokens()) {
                arrInfo[yIdx].add(strToInt(arrLine.nextToken()));
            }

        }

        // 함수를 호출하여 결과를 확인
        int result = findMinCost(arrInfo);

        // 결과 출력
        output.write(Integer.toString(result));
        output.flush();
        output.close();

    }

}