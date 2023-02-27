import java.io.*;
import java.util.*;

public class Main {

    public static int dfs(int nowNode, int parent, boolean[] visitLog, HashMap<Integer, ArrayList<Integer>> graph) {

        for (int nextNode : graph.get(nowNode)) {

            if (nextNode != parent && !visitLog[nextNode]) {

                visitLog[nextNode] = true;

                int result = dfs(nextNode, nowNode, visitLog, graph);
                if (result == 0) {
                    return 0;
                }

            } else if (nextNode != parent && visitLog[nextNode]) {
                return 0;
            }

        }

        return 1;

    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        int testCase = 0;

        ArrayList<String> outputArr = new ArrayList<>();

        while (true) {

            StringTokenizer treeInfo = new StringTokenizer(input.readLine(), "[ ]");
            int nodeNumber = Integer.parseInt(treeInfo.nextToken());
            int edgeNumber = Integer.parseInt(treeInfo.nextToken());

            if (nodeNumber == 0 && edgeNumber == 0) {
                break;
            }

            testCase += 1;

            int treeCount = 0;
            boolean[] isVisited = new boolean[nodeNumber + 1];

            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append("Case ");
            stringBuilder.append(testCase);
            stringBuilder.append(": ");

            HashMap<Integer, ArrayList<Integer>> treeGraph = new HashMap<>();
            for (int i = 1; i < nodeNumber + 1; i++) {
                treeGraph.put(i, new ArrayList<>());
            }

            for (int i = 0; i < edgeNumber; i++) {

                StringTokenizer edgeInfo = new StringTokenizer(input.readLine(), "[ ]");
                int startNode = Integer.parseInt(edgeInfo.nextToken());
                int endNode = Integer.parseInt(edgeInfo.nextToken());

                treeGraph.get(startNode).add(endNode);
                treeGraph.get(endNode).add(startNode);

            }

            for (int i = 1; i < nodeNumber + 1; i++) {

                isVisited[i] = true;
                treeCount += dfs(i, 0, isVisited, treeGraph);
            }

            if (treeCount == 0) {
                stringBuilder.append("No trees.");
            } else if (treeCount == 1) {
                stringBuilder.append("There is one tree.");
            } else if (treeCount > 1) {
                stringBuilder.append("A forest of ");
                stringBuilder.append(treeCount);
                stringBuilder.append(" trees.");
            }

            outputArr.add(stringBuilder.toString());

        }

        for (int i = 0; i < testCase; i++) {

            if (i != testCase - 1) {
                output.write(outputArr.get(i) + "\n");
            } else {
                output.write(outputArr.get(i));
            }

        }

        output.flush();
        output.close();

    }

}
