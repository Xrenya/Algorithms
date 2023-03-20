class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for (int i = 0; i < flowerbed.size(); i++) {
            if (flowerbed[i] == 0) {
                bool left_side = (i == 0) || (flowerbed[i - 1] == 0);
                bool right_side = (i == flowerbed.size() - 1) || (flowerbed[i + 1] == 0);
                if (left_side && right_side) {
                    flowerbed[i] = 1;
                    n -= 1;
                    if (n == 0){
                        return true;
                    }
                }
            }
        }
        return  (n <= 0) ? true : false;
    }
};
