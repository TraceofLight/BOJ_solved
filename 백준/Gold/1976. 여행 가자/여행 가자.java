import java.io.*;
import java.util.*;

public class Main {

    // String to Integer 함수
    public static int strToInt(String target) {
        return Integer.parseInt(target);
    }

    // 조상 노드를 찾아가는 함수
    public static int findAncestor(ArrayList<Integer> unionList, int childNode) {

        int parent = unionList.get(childNode);

        if (parent != childNode) {
            unionList.set(childNode, findAncestor(unionList, parent));
        }

        return unionList.get(childNode);
    }

    // 두 노드의 집합을 합쳐주는 함수
    public static void unionCity(ArrayList<Integer> unionList, int target1, int target2) {

        int ancestor1 = findAncestor(unionList, target1);
        int ancestor2 = findAncestor(unionList, target2);

        // 두 노드의 집합이 다른 경우 집합을 하나로 합침
        if (ancestor1 != ancestor2) {

            if (ancestor1 > ancestor2) {
                unionList.set(ancestor1, ancestor2);
            } else {
                unionList.set(ancestor2, ancestor1);
            }

        }

    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        // 전체 도시 갯수, 여행 계획 도시 갯수 입력
        int totalCityNumber = strToInt(input.readLine());
        int planNumber = strToInt(input.readLine());

        // 집합 정보를 담을 리스트 선언
        ArrayList<Integer> unionArr = new ArrayList<>();

        // 각 원소를 -1로 초기화
        for (int i = 0; i <= totalCityNumber; i++) {
            unionArr.add(i);
        }

        // 도시 간 연결 정보 입력
        for (int city1 = 1; city1 <= totalCityNumber; city1 += 1) {

            StringTokenizer unionInfo = new StringTokenizer(input.readLine(), "[ ]");
            int city2 = 1;

            while (unionInfo.hasMoreTokens()) {

                int connectInfo = strToInt(unionInfo.nextToken());

                // 만약 두 도시가 연결된 상태라면 함수를 호출하여 원소값을 동일값으로 변경
                if (connectInfo == 1) {
                    unionCity(unionArr, city1, city2);
                }

                city2 += 1;

            }

        }

        // 여행 정보 입력
        StringTokenizer journeyPlan = new StringTokenizer(input.readLine(), "[ ]");

        // 여행 가능 여부 flag 선언
        boolean canGoTrip = true;

        // 첫 원소로부터 집합 정보 확인
        int unionNumber = findAncestor(unionArr, strToInt(journeyPlan.nextToken()));

        for (int i = 0; i < planNumber - 1; i++) {

            int nowUnion = findAncestor(unionArr, strToInt(journeyPlan.nextToken()));

            // 집합이 다르거나 존재하지 않는 경우 여행을 갈 수 없기 때문에 false 처리 후 break
            if (unionNumber != nowUnion) {
                canGoTrip = false;
                break;
            }

        }

        // 결과에 따라 출력
        if (canGoTrip) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

    }
}