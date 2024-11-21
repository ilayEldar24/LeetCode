typedef struct {
    int* heap;
    int k;
    int curSize;
} KthLargest;

void push(KthLargest* heapst, int val) {
    if (heapst->curSize < heapst->k) {
        // Insert the new value directly
        heapst->heap[heapst->curSize] = val;
        int curIdx = heapst->curSize;

        // Bubble up
        while (curIdx > 0) {
            int parentIdx = (curIdx - 1) / 2;
            if (heapst->heap[curIdx] >= heapst->heap[parentIdx]) break;

            // Swap values
            int tmp = heapst->heap[curIdx];
            heapst->heap[curIdx] = heapst->heap[parentIdx];
            heapst->heap[parentIdx] = tmp;
            curIdx = parentIdx;
        }
        heapst->curSize++;
    } else if (val > heapst->heap[0]) {
        // Replace root and bubble down
        heapst->heap[0] = val;
        int curIdx = 0;

        while (curIdx < heapst->k) {
            int leftChildIdx = curIdx * 2 + 1;
            int rightChildIdx = curIdx * 2 + 2;
            int smallest = curIdx;

            if (leftChildIdx < heapst->curSize && heapst->heap[leftChildIdx] < heapst->heap[smallest]) {
                smallest = leftChildIdx;
            }
            if (rightChildIdx < heapst->curSize && heapst->heap[rightChildIdx] < heapst->heap[smallest]) {
                smallest = rightChildIdx;
            }
            if (smallest == curIdx) break;

            // Swap values
            int tmp = heapst->heap[curIdx];
            heapst->heap[curIdx] = heapst->heap[smallest];
            heapst->heap[smallest] = tmp;
            curIdx = smallest;
        }
    }
}

KthLargest* kthLargestCreate(int k, int* nums, int numsSize) {
    KthLargest* res = (KthLargest*)malloc(sizeof(KthLargest));
    res->heap = (int*)malloc(k * sizeof(int));
    res->curSize = 0;
    res->k = k;

    for (int i = 0; i < numsSize; i++) {
        push(res, nums[i]);
    }
    return res;
}

int kthLargestAdd(KthLargest* obj, int val) {
    push(obj, val);
    return obj->heap[0];
}

void kthLargestFree(KthLargest* obj) {
    free(obj->heap);
    free(obj);
}
