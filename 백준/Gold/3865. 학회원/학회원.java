import java.io.*;
import java.util.*;

public class Main {

    /**
     * 해당 학회의 총 인원수를 반환하는 함수
     */

    public static int getTotalPerson(String target) {

        // 결과값 변수 선언
        int result = 0;

        // 아직 방문하지 않은 경우에 대해서만 처리
        if (!visitLog.contains(target)) {

            // 방문 기록
            visitLog.add(target);

            // 사람이 아닌 학회일 경우
            if (clubGraph.containsKey(target)) {

                // 해당 학회의 방문하지 않은 구성원에 대해 재귀함수를 호출, 결과값에 합산
                for (String eachPerson : clubGraph.get(target)) {

                    // 구성원이 학회라면 재귀함수 호출
                    if (clubGraph.containsKey(eachPerson)) {
                        result += getTotalPerson(eachPerson);

                    // 학생이라면 아직 방문하지 않았을 경우 결과값 1 추가
                    } else {

                        if (!visitLog.contains(eachPerson)) {

                            visitLog.add(eachPerson);
                            result += 1;

                        }

                    }

                }

            }

        }

        // 결과값을 반환
        return result;

    }

    public static int strToInt(String inputString) {
        return Integer.parseInt(inputString);
    }

    // 학회 수, 첫 학회, 학회 관계 그래프, 학생 기록 집합 정적 변수 선언
    static int clubNumber;
    static String firstClub;
    static HashMap<String, ArrayList<String>> clubGraph = new HashMap<>();
    static Set<String> visitLog = new HashSet<>();

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        // 학회의 수 입력, 입력값이 0이라면 반복 종료
        while ((clubNumber = strToInt(input.readLine())) != 0) {

            clubGraph.clear();
            visitLog.clear();

            for (int i = 0; i < clubNumber; i++) {

                // 줄 단위 입력
                StringTokenizer clubInfo = new StringTokenizer(input.readLine(),"[:,.]");

                // 학회 이름 변수 선언
                String clubName = clubInfo.nextToken();

                // 첫 학회라면 따로 변수에 기록
                if (i == 0) {
                    firstClub = clubName;
                }

                // 기존에 없던 학회라면 추가
                if (!clubGraph.containsKey(clubName)) {
                    clubGraph.put(clubName, new ArrayList<>());
                }

                // 나머지를 전부 학회의 원소로 추가
                while (clubInfo.hasMoreTokens()) {
                    clubGraph.get(clubName).add(clubInfo.nextToken());
                }

            }

            // 함수를 호출하여 결과값을 출력 스택에 추가
            System.out.println(getTotalPerson(firstClub));

        }

    }

}