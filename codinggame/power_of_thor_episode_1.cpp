#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

int main()
{
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

    // game loop
    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        if (initial_tx < light_x){
            if (initial_ty < light_y){
                initial_ty++;
                cout << "SE" << endl;
            }
            else if (initial_ty > light_y){
                cout << "NE" << endl;
                initial_ty--;
            }
            else{
                cout << "E" << endl;
                initial_tx++;
            }
        }
        else if (initial_tx > light_x){
            if (initial_ty < light_y){
                initial_ty++;
                cout << "SW" << endl;
            }
            else if (initial_ty > light_y){
                cout << "NW" << endl;
                initial_ty--;
            }
            else{
                cout << "W" << endl;
                initial_tx--;
            }
        }
        else{
            if (initial_ty > light_y){
                cout << "N" << endl;
                initial_ty--;
            }
            else{
                cout << "S" << endl;
                initial_ty++;
            }
        }

        // A single line providing the move to be made: N NE E SE S SW W or NW
        //cout << "SE" << endl;
    }
}
