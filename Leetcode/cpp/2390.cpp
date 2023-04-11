class Solution {
public:
    string removeStars(string s) {
      string new_s = "";
      int counter = 0;
      for (int i = s.size() - 1; i > -1; i--) {
        if (counter == 0 && s[i] != '*') {
          new_s += s[i];
        } else if (s[i] == '*') {
          counter += 1;
        } else {
          counter -= 1;
        }
      }
      reverse(new_s.begin(), new_s.end());
    return new_s;
    }
};
