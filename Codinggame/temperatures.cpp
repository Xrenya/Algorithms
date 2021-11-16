#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>     
using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int n; // the number of temperatures to analyse
    int out = 10001;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();
        if (abs(t) <= abs(out)){
            if (abs(out) == abs(t)){
                if (out < 0){
                    out = t;
                }
            }
            else{
                out = t;
            }
        }
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
    if (10001 == out){
        cout << 0 << endl;
    }
    else{
        cout << out << endl;
    }
}
