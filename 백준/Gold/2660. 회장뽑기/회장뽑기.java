import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        // 회원 수 입력
        int memberNumber = Integer.parseInt(input.readLine());

        // 관계 그래프 생성
        ArrayList<HashSet<Integer>> relationGraph = new ArrayList<>();
        for (int i = 0; i < memberNumber + 1; i++) {
            relationGraph.add(new HashSet<>());
        }

        // 관계 입력
        while (true) {

            StringTokenizer memberRelation = new StringTokenizer(input.readLine(), "[ ]");

            int member1 = Integer.parseInt(memberRelation.nextToken());
            int member2 = Integer.parseInt(memberRelation.nextToken());

            // "-1 -1" 이 입력된 경우 반복 종료
            if (member1 == -1 && member2 == -1) {
                break;
            } else {

                relationGraph.get(member1).add(member2);
                relationGraph.get(member2).add(member1);

            }

        }

        // 각 회원별 친구 관계 결과를 담을 배열 선언 및 더미값 입력
        int[] relationResult = new int[memberNumber + 1];
        relationResult[0] = 100;

        // 모든 회원들에 대해 확인
        for (int startMember = 1; startMember <= memberNumber; startMember++) {

            // Breadth First Search

            // 최대 관계 깊이 변수 및 방문 기록 리스트 선언
            int maxRelation = 0;
            boolean[] visited = new boolean[memberNumber + 1];

            // 너비 탐색을 위한 큐 선언 및 초기값 입력
            Queue<int[]> progressQue = new LinkedList<>();
            progressQue.add(new int[]{startMember, 0});
            visited[startMember] = true;

            // 큐가 빌 때까지 반복
            while (!progressQue.isEmpty()) {

                // 현재 회원 정보 확인
                int[] nowMemberInfo = progressQue.poll();
                int nowMember = nowMemberInfo[0];
                int relationDepth = nowMemberInfo[1];

                // 기존 깊이보다 크다면 갱신
                if (maxRelation < relationDepth) {
                    maxRelation = relationDepth;
                }

                // 방문하지 않은 다음 회원에 대해서 방문 처리 및 큐에 추가
                for (int nextMember : relationGraph.get(nowMember)) {

                    if (!visited[nextMember]) {
                        visited[nextMember] = true;
                        progressQue.add(new int[]{nextMember, relationDepth + 1});
                    }

                }

            }

            // 최대 관계 깊이를 배열 원소로 입력
            relationResult[startMember] = maxRelation;

        }

        // 회장 후보 점수 변수 및 회장 후보를 담을 배열 선언
        int candidateScore = 100;
        ArrayList<Integer> candidateList = new ArrayList<>();

        // 모든 회원에 대해서 확인
        for (int i = 0; i <= memberNumber; i++) {

            // 기존 점수보다 작은 값이 나왔다면 기존 후보 전부 제거 및 현재 후보 점수 입력, 배열에 추가
            if (candidateScore > relationResult[i]) {

                candidateScore = relationResult[i];
                candidateList.clear();
                candidateList.add(i);

                // 기존 점수와 같으면 배열에만 추가
            } else if (candidateScore == relationResult[i]) {

                candidateList.add(i);

            }

        }

        // 조건에 맞춰 결과 출력
        output.write(candidateScore + " " + candidateList.size() +"\n");

        for (int i = 0; i < candidateList.size() - 1; i++) {
            output.write(candidateList.get(i) + " ");
        }

        output.write(candidateList.get(candidateList.size() - 1).toString());

        output.flush();
        output.close();

    }

}