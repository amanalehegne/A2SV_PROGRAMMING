class TrieNode {
public:
    TrieNode() : children(2, nullptr), value(0) {}

    vector<TrieNode*> children;
    int value;
};

class Trie {
public:
    Trie() : root(new TrieNode()) {}

    void insert(int number) {
        TrieNode* node = root;
        for (int i = 31; i >= 0; --i) {
            int bit = (number >> i) & 1;
            if (!node->children[bit]) {
                node->children[bit] = new TrieNode();
            }
            node = node->children[bit];
        }
        node->value = number;
    }

    int search(int number) {
        TrieNode* node = root;
        int result = 0;
        for (int i = 31; i >= 0; --i) {
            int bit = (number >> i) & 1;
            int opposite_bit = 1 - bit;
            if (node->children[opposite_bit]) {
                node = node->children[opposite_bit];
                result |= (1 << i);
            } else {
                node = node->children[bit];
            }
        }
        return result;
    }

private:
    TrieNode* root;
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        int max_xor = INT_MIN;
        for (int num : nums) {
            trie.insert(num);
            max_xor = max(max_xor, trie.search(num));
        }
        return max_xor;
    }
};
