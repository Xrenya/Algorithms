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

# Пример использования
string = "abacaba"
actions = {1: 1, 2: 1, 3: 1, 4: 3, 5: 2, 6: 1, 7: 2}
total_actions = min_actions_to_construct_string(string, actions)
print("Минимальное количество действий:", total_actions)
