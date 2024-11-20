
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    struct TreeNode* cur = root;
    struct TreeNode* toInsert = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    toInsert->val = val;
    
    if(!root){
        toInsert->left = toInsert->right = NULL;
        return toInsert;
    }
    
    while (cur) {
        if (val < cur->val) {
            if (cur->left) cur = cur->left;
            else {
                cur->left = toInsert;
                toInsert->left = toInsert->right = NULL;
                return root;
            }
        }
        else {
            if (cur->right) cur = cur->right;
            else {
                cur->right = toInsert;
                toInsert->right = toInsert->left = NULL;
                return root;
            }
        }
    }
    
    return root;


}
