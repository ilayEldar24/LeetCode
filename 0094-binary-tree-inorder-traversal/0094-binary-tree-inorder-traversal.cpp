
class Solution {
public:

    void helper(vector<int>& arr, TreeNode* root) {
        if (!root) return;
        else {
            helper(arr, root->left);
            arr.push_back(root->val);
            helper(arr, root->right);
        }
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(res ,root);
        return res;
    }
};