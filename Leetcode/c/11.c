int maxArea(int* height, int heightSize) {
    int left = 0, right = heightSize - 1, max = 0;
    while (left < right) {
        int new_max = (right - left) * (height[left] < height[right] ? height[left] : height[right]);
        max = max < new_max ? new_max : max;
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max;
}
