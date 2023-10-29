def min_actions_to_construct_string(s, actions):
    actions_count = [0] * (len(s) + 1)  # Массив для хранения минимального количества действий
    
    # Перебираем каждую букву в строке
    for i in range(1, len(s) + 1):
        # Начальное количество действий, чтобы вставить букву i
        min_actions = actions[i]
        
        # Перебираем все возможные подстроки и находим минимальное количество действий
        for j in range(1, i):
            min_actions = min(min_actions, actions_count[j] + actions[i - j])
        
        actions_count[i] = min_actions
    
    # Возвращаем минимальное количество действий, чтобы построить всю строку
    return actions_count[len(s)]

def calculate_actions(string):
    n = len(string)
    actions = {}
    
    # Initialize actions for individual characters
    for i in range(n):
        actions[i + 1] = 1
    
    # Calculate actions for substrings of length > 1 using dynamic programming
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            substring = string[start:end + 1]
            actions[length] = min(actions.get(length, float('inf')), actions.get(length - 1, float('inf')) + 1)
            
            # Check if the substring can be compressed (e.g., "aaa" can be compressed to "a3")
            for sub_length in range(1, length):
                if length % sub_length == 0 and substring[:sub_length] * (length // sub_length) == substring:
                    actions[length] = min(actions.get(length, float('inf')), actions.get(sub_length, float('inf')) + 2)
    
    return actions

# Example usage
string = "abacaba"
actions = calculate_actions(string)
print("Actions dictionary:", actions)
# actions = {1: 1, 2: 1, 3: 1, 4: 3, 5: 2, 6: 1, 7: 2}
# В данном примере actions представляет собой словарь,
# где ключи - это длины подстрок, а значения - количество действий,
# необходимых для вставки подстроки.
# Функция min_actions_to_construct_string вычисляет минимальное количество действий,
# необходимых для построения всей строки s
total_actions = min_actions_to_construct_string(string, actions)
print("Минимальное количество действий:", total_actions)
