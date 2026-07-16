class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char, int> umapMag;

        for (auto chr : magazine) {
            ++umapMag[chr];
        }
        for (const auto& chr : ransomNote) {
            if (!umapMag.contains(chr) || umapMag[chr] == 0) return false;
            --umapMag[chr];
        }

        return true;
    }
};

class SolutionV2 {
public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char, int> umapMag, umapRan;

        for (auto chr : magazine) {
            ++umapMag[chr];
        }
        for (auto chr : ransomNote) {
            ++umapRan[chr];
        }

        for (const auto& [key, value] : umapRan) {
            if (!umapMag.contains(key) || umapMag[key] < value) {
                return false;
            }
        }
        return true;
    }
};
