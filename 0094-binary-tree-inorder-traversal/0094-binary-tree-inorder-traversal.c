void helper_inorder(struct TreeNode* root, int* arr, int* counter) {
     if (!root) return;
     else{
         helper_inorder(root->left, arr, counter);
         arr[*(counter)] = root->val;
         *counter += 1;
         helper_inorder(root->right, arr, counter);
     }

 }
 int* inorderTraversal(struct TreeNode* root, int* returnSize) {
     int* arr = (int*)malloc(100 * sizeof(int));
     int counter = 0;

     helper_inorder(root, arr, &counter);

     *returnSize = counter;
     arr = (int*)realloc(arr, counter * sizeof(int));
     return arr;
 }
