class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int Pf = INT_MIN;
        int Ps = INT_MIN;
        int Pt = INT_MIN;

        int Nf = INT_MAX;
        int Ns = INT_MAX;
        int Nt = INT_MAX;

        for (const auto& n : nums) {
            if (Pf <= n) {
                Pt = Ps;
                Ps = Pf;
                Pf = n;
            } else if (Ps <= n) {
                Pt = Ps;
                Ps = n;
            } else if (Pt <= n) {
                Pt = n;
            }

            
            if (Nf >= n) {
                Nt = Ns;
                Ns = Nf;
                Nf = n;
            } else if (Ns >= n) {
                Nt = Ns;
                Ns = n;
            } else if (Nt >= n) {
                Nt = n;
            }
        }
        int maxValue = std::max<int>(Pf * Ps * Pt, Nf * Ns * Nt);
        maxValue = std::max<int>(maxValue, Nf * Ns * Pf);
        return maxValue;
    }
};
