/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    std::unordered_map<Node*, Node*> umap; 
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return node;
        }
        if (umap.contains(node)) {
            return umap[node];
        }
        Node* add_node = new Node(node->val);;
        umap[node] = add_node;
        for (const auto& nei : node->neighbors) {
            add_node->neighbors.push_back(cloneGraph(nei));
        }
        return add_node;
    }
};
