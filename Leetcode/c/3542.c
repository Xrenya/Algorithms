int minOperations(int* nums, int numsSize) {
    int ops = 0;
    int* queue = (int*)malloc(sizeof(int) * numsSize);
    int index = 0;
    for (int i = 0; i < numsSize; ++i) {
      while (index > 0 && queue[index - 1] > nums[i]) {
        --index;
      }
      if (nums[i] == 0) continue;
      if (index == 0 || queue[index - 1] < nums[i]) {
        ops++;
        queue[index++] = nums[i];
      }
    }
    return ops;
}
