class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hashStudent = {0:0, 1:0}
        hashSandwich = {0:0, 1:0}
        
        for student in students:
            hashStudent[student] += 1
        
        for sandwich in sandwiches:
            hashSandwich[sandwich] += 1
                
        while True:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
                if hashSandwich[sandwiches[0]] > 0 and hashStudent[sandwiches[0]] == 0:
                    break
            else:
                students.pop(0)
                firstS = sandwiches.pop(0)
                hashSandwich[firstS] -= 1
                hashStudent[firstS] -= 1
                if len(students) == 0:
                    break
        return hashStudent[0] + hashStudent[1]
    
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        hashStudent = {0:0, 1:0}
        hashSandwich = {0:0, 1:0}
        
        for student in students:
            hashStudent[student] += 1
        
        for sandwich in sandwiches:
            hashSandwich[sandwich] += 1
                
        flag = True 
        while flag:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
                if hashSandwich[sandwiches[0]] > 0 and hashStudent[sandwiches[0]] == 0:
                    break
            else:
                students.pop(0)
                firstS = sandwiches.pop(0)
                hashSandwich[firstS] -= 1
                hashStudent[firstS] -= 1
                if len(students) == 0:
                    break
        return hashStudent[0] + hashStudent[1]
    
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        hashStudent = {0:0, 1:0}
        hashSandwich = {0:0, 1:0}
        
        for student in students:
            hashStudent[student] += 1
        
        for sandwich in sandwiches:
            hashSandwich[sandwich] += 1
                
        flag = True 
        while flag:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
                if hashSandwich[sandwiches[0]] > 0 and hashStudent[sandwiches[0]] == 0:
                    flag = False
                    break
            else:
                students.pop(0)
                firstS = sandwiches.pop(0)
                hashSandwich[firstS] -= 1
                hashStudent[firstS] -= 1
                if len(students) == 0:
                    flag = False
                    break
        return hashStudent[0] + hashStudent[1]
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        hashStudent = collections.Counter(students)
        hashSandwich = collections.Counter(sandwiches)
         
        while True:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
                if hashSandwich[sandwiches[0]] > 0 and hashStudent[sandwiches[0]] == 0:
                    break
            else:
                students.pop(0)
                firstS = sandwiches.pop(0)
                hashSandwich[firstS] -= 1
                hashStudent[firstS] -= 1
                if len(students) == 0:
                    break
        return hashStudent[0] + hashStudent[1]
