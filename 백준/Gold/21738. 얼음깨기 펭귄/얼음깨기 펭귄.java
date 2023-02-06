import java.io.*;
import java.util.*;

public class Main {

    static ArrayList<Integer> shortPathArray = new ArrayList<>();

    public static void breadthFirstSearch(ArrayList<ArrayList<Integer>> targetGraph,
                                          int nowNode,
                                          int parentNode,
                                          int targetNode,
                                          int count) {

        if (nowNode == targetNode) {
            shortPathArray.add(count);
        } else {
            for (int nextNode : targetGraph.get(nowNode)) {
                if (nextNode != parentNode) {
                    breadthFirstSearch(targetGraph, nextNode, nowNode, targetNode, count + 1);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer penguinInfo = new StringTokenizer(input.readLine(), "[ ]");
        int IceNumber = Integer.parseInt(penguinInfo.nextToken());
        int stableBlock = Integer.parseInt(penguinInfo.nextToken());
        int nowPenguin = Integer.parseInt(penguinInfo.nextToken());

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < IceNumber + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < IceNumber - 1; i++) {

            StringTokenizer connectionInfo = new StringTokenizer(input.readLine(), "[ ]");

            int startIce = Integer.parseInt(connectionInfo.nextToken());
            int endIce = Integer.parseInt(connectionInfo.nextToken());

            graph.get(startIce).add(endIce);
            graph.get(endIce).add(startIce);

        }

        for (int i = 1; i < stableBlock + 1; i++) {
            breadthFirstSearch(graph, i, -1, nowPenguin, 0);
        }

        Collections.sort(shortPathArray);

        int result = IceNumber - 1;

        for (int i = 0; i < 2; i++) {
            result -= shortPathArray.get(i);
        }

        output.write(Integer.toString(result));

        output.flush();
        output.close();

    }

}
