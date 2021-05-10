class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '')
        number = number.replace(' ', '')
        string = ''
        while len(number) > 4:
            string += number[:3] + '-'
            number = number[3:]
        if len(number) == 4:
            string += number[:2] + '-' + number[2:4]
        else:
            string += number
        return string

class Solution:
    # Recursion
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '')
        number = number.replace(' ', '')
        phone_str = ''
        return self.solver(phone_str, number)
        
    def solver(self, phone_str, number):
        if len(number) == 2 or len(number) == 3:
            return number
        elif len(number) == 4:
            return number[:2] + '-' + number[2:]
        else:
            phone_str = number[:3]
            number = number[3:]
            return phone_str + '-' + self.solver(phone_str, number)
            
        
        
