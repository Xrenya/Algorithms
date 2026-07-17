class Solution {
public:
    string simplifyPath(string path) {
        vector<string> dirOrFiles;
        stringstream ss(path);
        string dirOrFile;
        while (getline(ss, dirOrFile, '/')) {
            if (!dirOrFiles.empty() && dirOrFile == "..") {
                dirOrFiles.pop_back();
            } else if (dirOrFile != "." && dirOrFile != "" && dirOrFile != "..") {
                dirOrFiles.push_back(dirOrFile);
            }
        }
        string simplified_path = "";
        for (string dirOrFile : dirOrFiles) {
            simplified_path += "/" + dirOrFile;
        }
        return simplified_path.empty() ? "/" : simplified_path;
    }
};

class SolutionV2 {
public:
    string simplifyPath(string path) {
        std::vector<std::string> buffer;
        std::stringstream ss(path);
        std::string segment;
        
        while (std::getline(ss, segment, '/')) {
            if (segment == "..") {
                if (!buffer.empty()) {
                    buffer.pop_back();
                }
            } else if (segment == ".") {
                continue;
            } else if (segment != "") {
                buffer.push_back(segment);
            }
        }
        
        std::string output;
        if (buffer.empty()) output += "/";
        for (const auto c : buffer) {
            output += "/" + c;
        }
        return output;
    }
};
