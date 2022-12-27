import java.io.*;
import java.util.*;

public class Main {

    public static class Node {

        char nowChar;
        HashSet<Node> childSet;
        String value;
        boolean isUnique = true;
        int count = 0;

        Node() {

            this.childSet = new HashSet<>();
            this.value = "";
            this.isUnique = false;

        }

        Node(char target) {

            this.nowChar = target;
            this.childSet = new HashSet<>();
            this.value = "";

        }

    }

    public static class Trie {

        Node head = new Node();

        public void addString(String target) {

            Node nowNode = this.head;
            int targetLength = target.length();

            for (int i = 0; i <= targetLength; i++) {

                if (i == targetLength) {

                    nowNode.count += 1;
                    nowNode.value = target;

                } else {

                    boolean hasChild = false;

                    for (Node subNode : nowNode.childSet) {

                        if (subNode.nowChar == target.charAt(i)) {

                            nowNode = subNode;
                            hasChild = true;
                            break;

                        }

                    }

                    if (!hasChild) {

                        Node madeNode = new Node(target.charAt(i));
                        nowNode.childSet.add(madeNode);
                        nowNode = madeNode;

                    }

                }

            }

        }

        public String findUnique(String target) {

            Node nowNode = this.head;
            int targetLength = target.length();
            boolean isFirstTime = true;
            int result = -1;
            int resultCount = -1;

            for (int i = 0; i < targetLength + 1; i++) {

                if (nowNode.isUnique && isFirstTime) {

                    nowNode.isUnique = false;
                    isFirstTime = false;
                    result = i;
                    resultCount = nowNode.count;

                } else {

                    if (nowNode.isUnique) {
                        nowNode.isUnique = false;
                    }

                }

                if (i == targetLength) {

                    if (result == -1) {
                        result = targetLength;
                        resultCount = nowNode.count;
                    }

                    if (nowNode.count == 1) {
                        return target.substring(0, result);

                    } else {
                        return target + resultCount;
                    }

                } else {

                    for (Node subNode : nowNode.childSet) {

                        if (subNode.nowChar == target.charAt(i)) {
                            nowNode = subNode;
                            break;

                        }

                    }

                }

            }

            return "NOT RUNNING";

        }

    }

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));

        Trie nickNameTrie = new Trie();

        int userNumber = Integer.parseInt(input.readLine());

        for (int i = 0; i < userNumber; i++) {

            String nickName = input.readLine();
            nickNameTrie.addString(nickName);

            if (i == userNumber - 1) {
                output.write(nickNameTrie.findUnique(nickName));

            } else {
                output.write(nickNameTrie.findUnique(nickName) + "\n");
            }

        }

        output.flush();
        output.close();

    }
}