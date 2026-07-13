"""
Implement a K-Means clustering algorithm from scratch.
The algorithm should take the following parameters:
a list of 2D data points data_points, an integer k indicating
the number of clusters, and max_iterations,
the maximum number of iterations.
The output should be a list of integers,
where each integer represents the cluster label of the
corresponding data point in data_points.
"""
import numpy as np


class KMeans:
    def __init__(self, num_clusters: int = 2, max_iterations: int = 300, eps=10**-5):
        self.num_clusters = num_clusters
        self.max_iterations = max_iterations
        self.eps = eps
        
    def fit(self, data):
        data = np.array(data)
        indexes = np.random.choice(np.arange(len(data)), size=self.num_clusters, replace=False)
        centers = data[indexes]
        
        labels = np.zeros(len(data), dtype=int)
        
        prevCenters = np.zeros_like(centers) + np.inf
        for _ in range(self.max_iterations):
            p1 = data[:, np.newaxis, :]
            p2 = centers[np.newaxis, :, :]
            dist = self.ecludian(p1, p2)
            labels = np.argmin(dist, 1)
            
            newCenter = np.array(
                [
                    data[i == labels].mean(0) if np.any(i == labels) else centers[i]
                    for i in range(self.num_clusters)
                ]
            )
            delta = self.ecludian(centers, newCenter)
            if delta.max() <= self.eps:
                break
            
            prevCenters = centers
            centers = newCenter
        print(labels)
        return labels
        
    def ecludian(self, p1, p2):
        deltaX = (p1[..., 0] - p2[..., 0])**2
        deltaY = (p1[..., 1] - p2[..., 1])**2
        delta = np.sqrt(deltaX + deltaY)
        return delta
        
        
data = [[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]]
expectedOutput = [0, 0, 1, 1, 0, 1]

kmeans = KMeans()
output = kmeans.fit(data)
print(f"Output: {output}")
