import java.io.*;
import java.util.*;

public class Main {

    static int[] directionX = new int[]{1, -1, 0, 0};
    static int[] directionY = new int[]{0, 0, 1, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 행렬 크기 입력
        StringTokenizer rangeInfo = new StringTokenizer(input.readLine(), "[ ]");
        int height = Integer.parseInt(rangeInfo.nextToken());
        int width = Integer.parseInt(rangeInfo.nextToken());

        // 행렬 정보 입력
        int[][] mapInfo = new int[height][width];

        for (int i = 0; i < height; i++) {

            String lineInfo = input.readLine();

            for (int j = 0; j < width; j++) {
                mapInfo[i][j] = Integer.parseInt(lineInfo.substring(j, j + 1));
            }

        }

        // 결과 배열 및 방문 배열 선언
        int[][] resultInfo = new int[height][width];
        boolean[][] visited = new boolean[height][width];

        // 연결된 0의 갯수를 담은 리스트의 주소값을 반환하는 해시 선언
        int[][] idxCounterHash = new int[height][width];

        // 연결된 0의 갯수 정보를 담을 리스트 선언
        ArrayList<Integer> logCountArr = new ArrayList<>();

        // 현재의 주소를 가리키는 카운터 선언
        int logCounter = 0;

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {

                // 방문하지 않은 0을 확인
                if (!visited[i][j] && mapInfo[i][j] == 0) {

                    // 방문 저리
                    visited[i][j] = true;

                    // 스택에 추가 및 해당 좌표에 대해 해시 연결
                    Stack<int[]> progressStack = new Stack<>();
                    progressStack.push(new int[] {i, j});
                    idxCounterHash[i][j] = logCounter;

                    // 연결된 0 카운터 선언
                    int zeroCounter = 1;

                    // Depth First Search
                    while (!progressStack.isEmpty()) {

                        int[] nowIdx = progressStack.pop();
                        int nowY = nowIdx[0];
                        int nowX = nowIdx[1];

                        for (int k = 0; k < 4; k++) {

                            int nextY = nowY + directionY[k];
                            int nextX = nowX + directionX[k];

                            if (0 <= nextY && nextY < height && 0 <= nextX && nextX < width) {

                                if (!visited[nextY][nextX] && mapInfo[nextY][nextX] == 0) {

                                    visited[nextY][nextX] = true;

                                    progressStack.push(new int[]{nextY, nextX});
                                    idxCounterHash[nextY][nextX] = logCounter;
                                    zeroCounter += 1;

                                }

                            }

                        }

                    }

                    // 현재 주소가 가리키는 지점에 연결된 0의 갯수 입력
                    logCountArr.add(zeroCounter);
                    logCounter += 1;

                }

            }
        }

        // 같은 주소 반복 접근 제어용 집합 선언
        HashSet<Integer> hashInfo = new HashSet<>();

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {

                // 0이 아닌 지점은 전부 0 처리
                if (mapInfo[i][j] == 0) {
                    resultInfo[i][j] = 0;
                } else {

                    hashInfo.clear();

                    // 집합에 주변 좌표들이 가리키는 주소값을 전부 추가
                    for (int k = 0; k < 4; k++) {

                        int nextY = i + directionY[k];
                        int nextX = j + directionX[k];

                        if (0 <= nextY && nextY < height && 0 <= nextX && nextX < width && mapInfo[nextY][nextX] == 0) {
                            hashInfo.add(idxCounterHash[nextY][nextX]);
                        }

                    }

                    // 중복을 제외한 주소에 존재하는 값을 전부 합산하여 결과 배열에 반영
                    resultInfo[i][j] = 1;

                    Iterator<Integer> hashSetIterator = hashInfo.iterator();

                    while (hashSetIterator.hasNext()) {
                        resultInfo[i][j] += logCountArr.get(hashSetIterator.next());
                    }

                    resultInfo[i][j] %= 10;

                }

            }
        }

        // 출력
        for (int i = 0; i < height; i++) {

            StringBuilder stringLine = new StringBuilder();

            for (int j = 0; j < width; j++) {

                if (j == width - 1) {
                    stringLine.append(resultInfo[i][j]);
                    output.write(stringLine + "\n");
                } else {
                    stringLine.append(resultInfo[i][j]);
                }

            }
        }

        output.flush();
        output.close();

    }
}