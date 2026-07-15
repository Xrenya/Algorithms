class Solution {
public:
    std::vector<std::string> fullJustify(const std::vector<std::string>& words, int maxWidth) {
        std::vector<std::string> output;

        std::vector<std::string> line;
        int currentWidth = 0;
        int wordCounter = 0;
        for (int i = 0; i < words.size(); ++i) {
            std::string word = words[i];
            if ((currentWidth + word.length() + wordCounter) <= maxWidth) {
                currentWidth += word.length();
                ++wordCounter;
                line.push_back(word);
            } else {
                std::string formattedLine = "";

                if (wordCounter == 1) {
                    formattedLine += line[0];
                    formattedLine.append(maxWidth - formattedLine.length(), ' ');
                } else {
                    int totalSpaces = maxWidth - currentWidth;
                    int baseSpaces = totalSpaces / (wordCounter - 1);
                    int extraSpaces = totalSpaces % (wordCounter - 1);
                    for (int j = 0; j < line.size(); ++j) {
                        formattedLine += line[j];
                        if (j != line.size() - 1) {
                            formattedLine.append(baseSpaces, ' ');
                        }
                        if (extraSpaces > 0) {
                            formattedLine += " ";
                            --extraSpaces;
                        }
                    }
                }

                currentWidth = 0;
                wordCounter = 0;
                line.clear();
                
                
                currentWidth += word.length();
                ++wordCounter;
                line.push_back(word);
                output.push_back(formattedLine);
            }
        }
        if (line.size() != 0) {
            std::string formattedLine = "";
            if (wordCounter == 1) {
                formattedLine += line[0];
                formattedLine.append(maxWidth - formattedLine.length(), ' ');
            } else {
                int leftSpaces = maxWidth - currentWidth - (wordCounter - 1);
                for (int j = 0; j < line.size(); ++j) {
                    formattedLine += line[j];
                    if (j != line.size() - 1) {
                        formattedLine.append(1, ' ');
                    }
                }
                formattedLine.append(leftSpaces, ' ');
            }
            output.push_back(formattedLine);
        }
        return output;
    }
   
};
