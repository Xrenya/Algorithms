#include <iostream>
#include <cassert>
#include <cmath>
#include <random>
#include <algorithm>
#include <vector>

class KMeans {
private:
    int k = 2;
    int maxIterations = 300;
    double eps = 0.00001;

public:
    KMeans() = default;
    KMeans(int k, int maxIterations, double eps) : k(k), maxIterations(maxIterations), eps(eps) { }
    
    std::vector<int> fit(const std::vector<std::vector<double>>& data) {
        std::random_device rd;  // <random>
        std::mt19937 gen(rd());  // <random>
        std::vector<int> indexes;
        for (int i = 0; i < data.size(); ++i) {
            indexes.push_back(i);
        }
        std::shuffle(indexes.begin(), indexes.end(), gen); // <algorithm>
        
        std::vector<int> labels(data.size(), 0);
        std::vector<std::vector<double>> center(k, std::vector<double>(2, 0));
        std::vector<std::vector<double>> newCenter(k, std::vector<double>(2, 0));

        
        std::vector<std::vector<double>> distance(data.size(), std::vector<double>(k, 0));

        for (int i = 0; i < k; ++i) {
            center[i] = data[indexes[i]];
        }

        for (int i = 0; i < maxIterations; ++i) {
            // calc dist
            for (int j = 0; j < data.size(); ++j) {
                for (int c = 0; c < k; ++c) {
                    double distX = pow(data[j][0] - center[c][0], 2);
                    double distY = pow(data[j][1] - center[c][1], 2);
                    distance[j][c] = pow(distX + distY, 0.5);
                }
            }
            // calc labels
            for (int j = 0; j < data.size(); ++j) {
                double minDist = distance[j][0];
                int label = 0;
                for (int c = 1; c < k; ++c) {
                    if (minDist > distance[j][c]) {
                        label = c;
                        minDist = distance[j][c];
                    }
                }
                labels[j] = label;
            }
            
            // update centers
            for (int c = 0; c < k; ++c) {
                double totalX = 0.0;
                double totalY = 0.0;
                int counter = 0;
                for (int j = 0; j < data.size(); ++j) {
                    if (labels[j] == c) {
                        totalX += data[j][0];
                        totalY += data[j][1];
                        ++counter;
                    }
                }
                if (counter > 0) {
                    newCenter[c] = {totalX / counter, totalY / counter};
                } else {
                    newCenter[c] = center[c];
                }
            }

            // stop or update
            double maxDist = 0.0;
            for (int c = 0; c < k; ++c) {
                double distX = pow(newCenter[c][0] - center[c][0], 2);
                double distY = pow(newCenter[c][1] - center[c][1], 2);
                maxDist = std::max(maxDist, pow(distX + distY, 0.5));
            }
            if (maxDist < eps) {
                break;
            }
            center = newCenter;
        }
        return labels;

    }
    
};


int main() {
    std::vector<std::vector<double>> data = {{1.0, 2.0}, {1.5, 1.8}, {5.0, 8.0}, {8.0, 8.0}, {1.0, 0.6}, {9.0, 11.0}};
    KMeans kmeans;

    std::vector<int> labels = kmeans.fit(data);
    std::cout << "Labels: ";
    for (int label : labels) {
        std::cout << label << " ";
    }
    std::cout << std::endl;
    // expectedOutput = [0, 0, 1, 1, 0, 1]
    return 0;
}
