#include <string>
#include <vector>

using namespace std;

class Solution {
private:
    long long MOD = 1000000007;

public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.length();

        // 1. Проекция индексов: маппинг из исходной строки в отфильтрованную
        // next_non_zero[i] указывает на индекс ближайшей НЕ-ноль цифры справа (включая i)
        // prev_non_zero[i] указывает на индекс ближайшей НЕ-ноль цифры слева (включая i)
        vector<int> next_non_zero(n, -1);
        vector<int> prev_non_zero(n, -1);
        
        int last = -1;
        for (int i = 0; i < n; ++i) {
            if (s[i] != '0') last = i;
            prev_non_zero[i] = last;
        }
        last = -1;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] != '0') last = i;
            next_non_zero[i] = last;
        }

        // 2. Строим отфильтрованную строку (без нулей) и карту индексов
        string filtered = "";
        vector<int> to_filtered(n, -1); // Ссылка из s[i] в filtered[j]
        for (int i = 0; i < n; ++i) {
            if (s[i] != '0') {
                to_filtered[i] = filtered.length();
                filtered += s[i];
            }
        }

        int m = filtered.length();
        if (m == 0) {
            // Если в строке вообще нет ненулевых цифр, все ответы — 0
            return vector<int>(queries.size(), 0);
        }

        // 3. Предподсчет степеней десятки по модулю MOD
        vector<long long> pow10(m + 1, 1);
        for (int i = 1; i <= m; ++i) {
            pow10[i] = (pow10[i - 1] * 10) % MOD;
        }

        // 4. Предподсчет префиксных сумм и префиксных чисел (хэшей)
        vector<long long> pref_sum(m + 1, 0);
        vector<long long> pref_num(m + 1, 0);

        for (int i = 0; i < m; ++i) {
            int digit = filtered[i] - '0';
            pref_sum[i + 1] = pref_sum[i] + digit;
            pref_num[i + 1] = (pref_num[i] * 10 + digit) % MOD;
        }

        // 5. Обработка запросов за O(1) каждый
        vector<int> output;
        output.reserve(queries.size());

        for (const auto& query : queries) {
            int left = query[0];
            int right = query[1];

            // Находим границы реальных ненулевых цифр внутри диапазона [left, right]
            int actual_left_idx = next_non_zero[left];
            int actual_right_idx = prev_non_zero[right];

            // Если в диапазоне только нули или индексы вышли за границы окна
            if (actual_left_idx == -1 || actual_right_idx == -1 || actual_left_idx > right || actual_right_idx < left) {
                output.push_back(0);
                continue;
            }

            // Переводим индексы исходной строки в индексы массива filtered
            int L = to_filtered[actual_left_idx];
            int R = to_filtered[actual_right_idx];

            // Вычисляем сумму цифр (mult) за O(1)
            long long mult = pref_sum[R + 1] - pref_sum[L];

            // Вычисляем значение получившегося числа (num) за O(1)
            long long num = (pref_num[R + 1] - (pref_num[L] * pow10[R - L + 1]) % MOD + MOD) % MOD;

            // Итоговый результат для запроса
            long long res = ((mult % MOD) * num) % MOD;
            output.push_back(res);
        }

        return output;
    }
};
