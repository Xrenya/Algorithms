class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        flag = False
        if cols%2 != 0:
            flag = True
        for row in range(rows):
            if flag:
                image[row][cols//2] = 1 ^ image[row][cols//2]
            for col in range(cols//2):
                temp = image[row][col]
                image[row][col] = 1 ^ image[row][cols-col-1]
                image[row][cols-col-1] = 1 ^ temp
        return image
      
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        hashMap = {0:1, 1:0}
        rows = len(image)
        cols = len(image[0])
        for row in range(rows):
            for col in range(cols//2):
                temp = image[row][col]
                image[row][col] = image[row][cols-col-1]
                image[row][cols-col-1] = temp
        for row in range(rows):
            for col in range(cols):
                image[row][col] = hashMap[image[row][col]]
        return image
      
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        hashMap = {0:1, 1:0}
        rows = len(image)
        cols = len(image[0])
        flag = False
        if cols%2 != 0:
            flag = True
        for row in range(rows):
            if flag:
                image[row][cols//2] = hashMap[image[row][cols//2]]
            for col in range(cols//2):
                temp = image[row][col]
                image[row][col] = hashMap[image[row][cols-col-1]]
                image[row][cols-col-1] = hashMap[temp]
        return image
