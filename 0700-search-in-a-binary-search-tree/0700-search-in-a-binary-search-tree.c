struct TreeNode* searchBST(struct TreeNode* root, int val) {

    struct TreeNode* cur = root;
    while (cur) {
        if (cur->val == val) return cur;
        else if (cur->val > val) {
            cur = cur->left;
        }
        else cur = cur->right;
    }
    return NULL;
}