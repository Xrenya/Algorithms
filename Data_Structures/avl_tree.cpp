#include <iostream>
#include <queue>
#include <algorithm> // для std::max

template <typename T>
class Node {
public:
    T data;
    int height = 1; // Новые узлы всегда имеют высоту 1
    Node<T>* left = nullptr;
    Node<T>* right = nullptr;

    Node(T data) : data(data) { }
    ~Node() { }
};

template <typename T>
class AVLTree {
public:
    Node<T>* root = nullptr;

    AVLTree() = default;

    // Вспомогательная функция для безопасного получения высоты (для nullptr высота = 0)
    int get_height(Node<T>* node) {
        return node ? node->height : 0;
    }

    // Вычисление баланс-фактора узла
    int get_balance(Node<T>* node) {
        return node ? get_height(node->left) - get_height(node->right) : 0;
    }

    // Обновление высоты узла на основе его детей
    void update_height(Node<T>* node) {
        if (node) {
            node->height = 1 + std::max(get_height(node->left), get_height(node->right));
        }
    }

    // Правое вращение (применяется при левом дисбалансе)
    Node<T>* rotate_right(Node<T>* y) {
        Node<T>* x = y->left;
        Node<T>* T2 = x->right;

        // Вращение
        x->right = y;
        y->left = T2;

        // Обновление высот
        update_height(y);
        update_height(x);

        return x; // Новый корень поддерева
    }

    // Левое вращение (применяется при правом дисбалансе)
    Node<T>* rotate_left(Node<T>* x) {
        Node<T>* y = x->right;
        Node<T>* T2 = y->left;

        // Вращение
        y->left = x;
        x->right = T2;

        // Обновление высот
        update_height(x);
        update_height(y);

        return y; // Новый корень поддерева
    }

    // Балансировка узла
    Node<T>* balance_node(Node<T>* node) {
        update_height(node);
        int balance = get_balance(node);

        // 1. Левый-Левый случай (LL) -> Одиночное правое вращение
        if (balance > 1 && get_balance(node->left) >= 0) {
            return rotate_right(node);
        }

        // 2. Левый-Правый случай (LR) -> Левое, затем правое вращение
        if (balance > 1 && get_balance(node->left) < 0) {
            node->left = rotate_left(node->left);
            return rotate_right(node);
        }

        // 3. Правый-Правый случай (RR) -> Одиночное левое вращение
        if (balance < -1 && get_balance(node->right) <= 0) {
            return rotate_left(node);
        }

        // 4. Правый-Левый случай (RL) -> Правое, затем левое вращение
        if (balance < -1 && get_balance(node->right) > 0) {
            node->right = rotate_right(node->right);
            return rotate_left(node);
        }

        return node; // Балансировка не требуется
    }

    // Публичный метод вставки
    void add(T value) {
        root = insert_recursive(root, value);
    }

    // Публичный метод удаления
    void del_node(T key) {
        root = delete_recursive(root, key);
    }

    // Вывод уровней дерева (BFS) с указанием текущей высоты узла
    void pprint_levels() {
        if (root == nullptr) return;
        std::queue<Node<T>*> q;
        q.push(root);

        while (!q.empty()) {
            int lenLevel = q.size();
            for (int i = 0; i < lenLevel; ++i) {
                Node<T>* curr = q.front();
                q.pop();

                std::cout << curr->data << "(h:" << curr->height << ") ";

                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }
            std::cout << std::endl;
        }
    }

private:
    // Рекурсивная вставка с последующей балансировкой
    Node<T>* insert_recursive(Node<T>* node, T value) {
        if (node == nullptr) {
            return new Node<T>(value);
        }

        if (value < node->data) {
            node->left = insert_recursive(node->left, value);
        } else if (value > node->data) {
            node->right = insert_recursive(node->right, value);
        } else {
            return node; // Дубликаты игнорируются
        }

        return balance_node(node);
    }

    // Поиск узла с минимальным значением (самый левый лист)
    Node<T>* find_min(Node<T>* node) {
        Node<T>* current = node;
        while (current->left != nullptr) {
            current = current->left;
        }
        return current;
    }

    // Рекурсивное удаление с последующей балансировкой
    Node<T>* delete_recursive(Node<T>* node, T key) {
        if (node == nullptr) return node;

        if (key < node->data) {
            node->left = delete_recursive(node->left, key);
        } else if (key > node->data) {
            node->right = delete_recursive(node->right, key);
        } else {
            // Узел найден!
            
            // Случай 1 и 2: Один или ноль потомков
            if (node->left == nullptr || node->right == nullptr) {
                Node<T>* temp = node->left ? node->left : node->right;

                if (temp == nullptr) { // Ноль потомков (лист)
                    temp = node;
                    node = nullptr;
                } else { // Один потомок
                    *node = *temp; // Копируем данные потомка в текущий узел
                }
                delete temp;
            } else {
                // Случай 3: Два потомка
                // Ищем минимальный элемент в правом поддереве
                Node<T>* temp = find_min(node->right);
                
                // Копируем его данные в текущий узел
                node->data = temp->data;
                
                // Удаляем этот минимальный узел-дубликат
                node->right = delete_recursive(node->right, temp->data);
            }
        }

        if (node == nullptr) return node;

        return balance_node(node);
    }
};

int main() {
    AVLTree<int> tree;

    // Вставляем элементы
    tree.add(5);
    tree.add(3);
    tree.add(6);
    tree.add(4);
    tree.add(2);

    std::cout << "Исходное AVL-дерево по уровням [Значение(высота)]:" << std::endl;
    tree.pprint_levels();

    // Удаляем элемент 3 (что спровоцирует перебалансировку)
    std::cout << "\nУдаляем узел 3..." << std::endl;
    tree.del_node(3);

    std::cout << "\nAVL-дерево после удаления:" << std::endl;
    tree.pprint_levels();

    return 0;
}
