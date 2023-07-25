class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int left = -1, right = arr.size(), m;
        while (left < right - 1) {
            m = left + (right - left) / 2;
            if (arr[m] < arr[m + 1]) {
                left = m;
            } else {
                right = m;
            }
        }
        return right;
    }
};
