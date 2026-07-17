#include <string>
#include <vector>
#include <cctype>

using namespace std;

class Solution {
public:
    int calculate(string s) {
        vector<int> stack;
        int current_result = 0;
        int sign = 1; // 1 означает '+', -1 означает '-'
        long long current_number = 0; // Использование long long защищает от overflow при парсинге чисел

        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];

            if (isdigit(c)) {
                // Формируем число по разрядам слева направо
                current_number = current_number * 10 + (c - '0');
            } 
            else if (c == '+') {
                // Применяем накопленное число к результату с текущим знаком
                current_result += sign * current_number;
                current_number = 0;
                sign = 1; // Следующее число будет со знаком '+'
            } 
            else if (c == '-') {
                current_result += sign * current_number;
                current_number = 0;
                sign = -1; // Следующее число будет со знаком '-'
            } 
            else if (c == '(') {
                // Сохраняем текущий промежуточный результат и знак перед скобками в стек
                stack.push_back(current_result);
                stack.push_back(sign);
                // Сбрасываем их для вычислений внутри скобок
                current_result = 0;
                sign = 1;
            } 
            else if (c == ')') {
                // Применяем последнее число внутри скобок
                current_result += sign * current_number;
                current_number = 0;

                // Достаем из стека знак перед скобкой и умножаем на результат внутри скобок
                int prev_sign = stack.back();
                stack.pop_back();
                current_result *= prev_sign;

                // Достаем из стека результат, посчитанный до скобок, и прибавляем к текущему
                int prev_result = stack.back();
                stack.pop_back();
                current_result += prev_result;
            }
        }

        // Если в конце строки осталось необработанное число, добавляем его
        if (current_number != 0) {
            current_result += sign * current_number;
        }

        return current_result;
    }
};
