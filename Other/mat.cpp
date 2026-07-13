#include <iostream>
#include <cassert>


class Matrix {
private:
    int rows {0};
    int cols  {0};
    int * data {nullptr};
    
public:
    Matrix() = default;
    Matrix(const int rows, const int cols) : rows(rows), cols(cols) {
        int size = rows * cols;
        this->data = new int[size]();  // initialize with zeros
        // this->data = new int[size];
        // for (int i = 0; i < size; ++i) {
        //     this->data[i] = 0;    
        // }
    }
    Matrix(const int rows, const int cols, const int * data) : rows(rows), cols(cols) {
        int size = rows * cols;
        this->data = new int[size];
        for (int i = 0; i < size; ++i) {
            this->data[i] = data[i];    
        }
        // std::copy(data, data + size, this->data);
    }
    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols) {
        if (other.data) {
            int size = rows * cols;
            this->data = new int[size];
            std::copy(other.data, other.data + size, this->data);
        } else {
            this->data = nullptr;
        }
    }
    Matrix& operator=(const Matrix& other) {
        if (this != &other) {
            delete[] data;
            rows = other.rows;
            cols = other.cols;
            if (other.data) {
                int size = rows * cols;
                data = new int[size];
                std::copy(other.data, other.data + size, data);
            } else {
                data = nullptr;
            }
        }
        return *this;
    }
    
    
    ~Matrix() {
        delete[] data;   
    }
    
    const int& get_value(int row, int col) const {
        int index = get(row, col);
        return data[index];
    }
    
    int& set_value(int row, int col) {
        int index = get(row, col);
        return data[index];
    }
    
    const int get(int row, int col) const {
        return row * cols + col;
    }
    
    
    void pprint() {
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                int index = get(row, col);
                std::cout << data[index] << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
    
    Matrix operator*(const Matrix& other) {
        assert(this->cols == other.rows && "Matrix dimensions must match for multiplication!");
        
        int newRows = this->rows;
        int newCols = other.cols;
        Matrix output(newRows, newCols);
        for (int i = 0; i < newRows; ++i) {
            for (int j = 0; j < newCols; ++j) {
                int acc = 0;
                for (int k = 0; k < cols; ++k) {
                    acc += (this->get_value(i, k) * other.get_value(k, j));
                }
                output.set_value(i, j) = acc;
            }
        }
        return output;
    }
    
    bool operator==(const Matrix& other) {
        if (this == &other) return true;
        if (rows != other.rows || cols != other.cols) {
            return false;
        }
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (this->get_value(i, j) != other.get_value(i, j)) {
                    return false;
                } 
            }
        }
        return true;;
    }
    
};


int main() {
    int rows = 4;
    int cols = 3;
    Matrix mat(rows, cols);
    
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            mat.set_value(i, j) = 1;
        }
        
    }
    mat.pprint();
    
    
    rows = 3;
    cols = 4;
    Matrix mat2(rows, cols);
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            mat2.set_value(i, j) = 1;
        }
        
    }
    mat2.pprint();
    
    
    Matrix ouptutMaxtrix = mat * mat2;
    ouptutMaxtrix.pprint();
    
    
    
    rows = 4;
    cols = 4;
    Matrix expectedMatrix(rows, cols);
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            expectedMatrix.set_value(i, j) = 3;
        }
        
    }
    assert((expectedMatrix == ouptutMaxtrix) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
