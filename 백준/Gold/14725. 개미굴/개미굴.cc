// 개미굴

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
  string value;
  vector<Node> next_nodes;

  static bool compare(const Node &a, const Node &b) {
    return lexicographical_compare(a.value.begin(),
                                   a.value.end(),
                                   b.value.begin(),
                                   b.value.end());
  }

  explicit Node(string val)
      : value(std::move(val)), next_nodes() {};
};

struct Trie {
  Node root;

  Trie() : root(std::move(Node(""))) {};

  void Print(Node &now_node, int depth) {
    if (&now_node != &root) {
      for (int i = 0; i < depth; i++)
        cout << "--";
      cout << now_node.value << endl;
    }

    sort(now_node.next_nodes.begin(),
         now_node.next_nodes.end(),
         Node::compare);

    for (Node &next_node : now_node.next_nodes) {
      Print(next_node, depth + 1);
    }
  }

  void Add(vector<string> &input_data) {
    Node *now_node = &root;
    for (string &now_data : input_data) {
      int find_node_number = -1;
      for (int i = 0; i < now_node->next_nodes.size(); i++) {
        if (now_node->next_nodes[i].value == now_data) {
          find_node_number = i;
          break;
        }
      }
      if (find_node_number != -1) {
        now_node = &now_node->next_nodes[find_node_number];
      } else {
        now_node->next_nodes.push_back(std::move(Node(now_data)));
        now_node = &now_node->next_nodes.back();
      }
    }
  }
};

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  Trie trie;
  int ant_number;
  cin >> ant_number;
  for (int i = 0; i < ant_number; i++) {
    int element_number;
    cin >> element_number;
    vector<string> temp_vector(element_number);
    for (int j = 0; j < element_number; j++) {
      cin >> temp_vector[j] ;
    }
    trie.Add(temp_vector);
  }
  trie.Print(trie.root, -1);
}
