import java.util.*;

public class Main {

    public static double distance(int point1x, int point1y, int point2x, int point2y) {
        /*
        두 점의 좌표가 주어졌을 때 두 점 사이의 거리를 반환하는 함수
         */
        double result;
        result = Math.sqrt(Math.pow(point2x - point1x, 2) + Math.pow(point2y - point1y, 2));
        return result;
    }

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // 3개의 점의 좌표 입력
        int[] coordInfo = new int[6];

        for (int i = 0; i < 6; i++) {
            coordInfo[i] = input.nextInt();
        }

        // 각 점 사이의 거리 확인 및 리스트화
        double distance1 = distance(coordInfo[0], coordInfo[1], coordInfo[2], coordInfo[3]);
        double distance2 = distance(coordInfo[0], coordInfo[1], coordInfo[4], coordInfo[5]);
        double distance3 = distance(coordInfo[2], coordInfo[3], coordInfo[4], coordInfo[5]);
        List<Double> distArr = Arrays.asList(distance1, distance2, distance3);

        // 거리 전체 합 확인
        double sumDist = distance1 + distance2 + distance3;

        // 거리 최대값이랑 최소값 따로 분류
        double maxDist = Collections.max(distArr);
        double minDist = Collections.min(distArr);

        // 만약 세 점이 한 직선 위에 위치한 경우
        if (
                (coordInfo[3] - coordInfo[1]) * (coordInfo[4] - coordInfo[0])
                == (coordInfo[5] - coordInfo[1]) * (coordInfo[2] - coordInfo[0])
        ) {

            System.out.println(-1);

        } else {

        // 거리값 중 하나가 대각선이 되므로 제일 짧은 변이 대각선이면 제일 길고 제일 긴 변이 대각선이면 제일 짧음
        double answer = 2 * (sumDist - minDist) - 2 * (sumDist - maxDist);

        // 결과 출력
        System.out.println(String.format("%.10f", answer));

        }

    }
}