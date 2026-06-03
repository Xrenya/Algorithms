#include <iostream>
#include <vector>
#include <limits>
#include <cassert>

class Solution {
public:
    int endingTime(std::vector<int>& start,
                   std::vector<int>& durationStart,
                   std::vector<int>& nextStart,
                   std::vector<int>& durationEnd) {
        int finish1 = std::numeric_limits<int>::max();
        for (int i = 0; i < start.size(); ++i) {
            finish1 = std::min<int>(finish1, start[i] + durationStart[i]);
        }
        int finish2 = std::numeric_limits<int>::max();
        for (int i = 0; i < nextStart.size(); ++i) {
            int tmp = std::max<int>(finish1, nextStart[i]) + durationEnd[i];
            finish2 = std::min<int>(finish2, tmp);
        }
        return finish2;
    }
    int earliestFinishTime(std::vector<int>& landStartTime,
                           std::vector<int>& landDuration,
                           std::vector<int>& waterStartTime,
                           std::vector<int>& waterDuration) {
        int first = endingTime(landStartTime, landDuration, waterStartTime, waterDuration);
        int second = endingTime(waterStartTime, waterDuration, landStartTime, landDuration);
        return std::min<int>(first, second);
    }
    int earliestFinishTimeV1(std::vector<int>& landStartTime,
                           std::vector<int>& landDuration,
                           std::vector<int>& waterStartTime,
                           std::vector<int>& waterDuration) {
        int n = static_cast<int>(landStartTime.size());
        int m = static_cast<int>(waterStartTime.size());
        int output = std::numeric_limits<int>::max();
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int water = waterStartTime[j] + waterDuration[j];
                int water2land = std::max<int>(water, landStartTime[i]) + landDuration[i];
                output = std::min<int>(output, water2land);

                int land = landStartTime[i] + landDuration[i];
                int land2water = std::max<int>(land, waterStartTime[j]) + waterDuration[j];
                output = std::min<int>(output, land2water);
            }
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::vector<int> landStartTime = {2, 8};
    std::vector<int> landDuration = {4, 1};
    std::vector<int> waterStartTime = {6};
    std::vector<int> waterDuration = {3};
    int exepectedOutput = 9;
    int otuput = sol.earliestFinishTimeV1(landStartTime, landDuration, waterStartTime, waterDuration);
    
    assert((exepectedOutput == otuput) && "Test #1 failed!");

    otuput = sol.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration);
    
    assert((exepectedOutput == otuput) && "Test #2 failed!");

    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
