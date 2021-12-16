#include <iostream>
#include <climits>

using namespace std;

int main() {
    int prev = INT_MAX, cur = 0;
    int inc = 0;
    
    while (cin >> cur) {
        if (prev < cur) inc++;
        prev = cur;
    }

    cout << inc << endl;
    
    return 0;
}
