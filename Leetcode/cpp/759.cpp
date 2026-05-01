#include <iostream>
#include <vector>

/*
// Definition for an Interval.
class Interval {
public:
    int start;
    int end;

    Interval() {}

    Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
public:
    std::vector<Interval> employeeFreeTime(std::vector<std::vector<Interval>> schedule) {
        std::vector<std::pair<int, int>> data;
        for (auto times : schedule) {
            for (auto time : times) {
                data.push_back({time.start, 1});
                data.push_back({time.end, -1});
            }
        }
        std::sort(data.begin(), data.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second;
        });
        std::vector<Interval> output;
        int last = -1;
        int total = 0;
        for (auto d : data) {
            total += d.second;
            if (last != -1) {
                Interval interv;
                interv.start = last;
                interv.end = d.first;
                output.push_back(interv);
                last = -1;
            } else if (total == 0 && last == -1) {
                last = d.first;
            }
        }
        return output;
    }
};
