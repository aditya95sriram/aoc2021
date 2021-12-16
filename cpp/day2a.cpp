#include <iostream>
#include <string>

using namespace std;

int main() {
    string command;
    int value = 0;
    int pos = 0, depth = 0;
    
    while (cin >> command >> value) {
        if (command.compare("up") == 0)
            depth -= value;
        else if (command.compare("down") == 0)
            depth += value;
        else
            pos += value;
    }

    cout << pos * depth << endl;

    return 0;
}
