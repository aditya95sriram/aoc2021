#include <iostream>
#include <string>

using namespace std;

int main() {
    string command;
    int value = 0;
    int pos = 0, depth = 0;
    int aim = 0;
    
    while (cin >> command >> value) {
        if (command.compare("up") == 0)
            aim -= value;
        else if (command.compare("down") == 0)
            aim += value;
        else {
            pos += value;
            depth += aim * value;
        }
    }

    cout << pos * depth << endl;

    return 0;
}
