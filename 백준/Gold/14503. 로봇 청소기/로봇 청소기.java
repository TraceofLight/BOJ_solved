import java.io.*;
import java.util.*;

public class Main {

    public static int height;
    public static int width;

    public static boolean isNeedClean(int[][] table, int nowYIndex, int nowXIndex) {
        return table[nowYIndex][nowXIndex] == 0;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer mapSize = new StringTokenizer(input.readLine(), "[ ]");

        // 뒷 방향 등록 해시맵 선언
        HashMap<Integer, Integer> backward = new HashMap<>();
        backward.put(0, 2);
        backward.put(2, 0);
        backward.put(1, 3);
        backward.put(3, 1);


        height = Integer.parseInt(mapSize.nextToken());
        width = Integer.parseInt(mapSize.nextToken());

        int[][] mapInfo = new int[height][width];

        StringTokenizer startingPoint = new StringTokenizer(input.readLine(), "[ ]");

        int nowY = Integer.parseInt(startingPoint.nextToken());
        int nowX = Integer.parseInt(startingPoint.nextToken());
        int nowDirection = Integer.parseInt(startingPoint.nextToken());

        for (int i = 0; i < height; i++) {
            StringTokenizer mapLine = new StringTokenizer(input.readLine(), "[ ]");

            for (int j = 0; j < width; j++) {
                mapInfo[i][j] = Integer.parseInt(mapLine.nextToken());
            }

        }

        int cleanCounter = 0;

        int[] directionY = new int[]{-1, 0, 1, 0};
        int[] directionX = new int[]{0, 1, 0, -1};

        Loop:
        while (true) {

            // 현재 칸이 청소가 필요하다면 청소 실시
            if (isNeedClean(mapInfo, nowY, nowX)) {
                mapInfo[nowY][nowX] = 2;
                cleanCounter += 1;
            }

            // 주변 칸에 대해서 확인
            for (int i = 1; i < 5; i++) {

                int targetDirection = (nowDirection + 4 - i) % 4;
                int targetY = nowY + directionY[targetDirection];
                int targetX = nowX + directionX[targetDirection];

                // 청소할 칸이 있는 경우 이동 및 방향 전환
                if (isNeedClean(mapInfo, targetY, targetX)) {
                    nowY = targetY;
                    nowX = targetX;
                    nowDirection = targetDirection;
                    break;
                }

                // 청소할 칸이 없는 경우 뒷칸 확인
                if (i == 4) {
                    targetY = nowY + directionY[backward.get(nowDirection)];
                    targetX = nowX + directionX[backward.get(nowDirection)];

                    // 뒤로 이동할 수 없는 경우 청소 종료
                    if (mapInfo[targetY][targetX] == 1) {
                        break Loop;

                        // 이동할 수 있다면 뒤로 1칸 후진
                    } else {
                        nowY = targetY;
                        nowX = targetX;
                    }
                }

            }

        }

        // 이동 결과 출력
        output.write(Integer.toString(cleanCounter));

        output.flush();
        output.close();

    }

}