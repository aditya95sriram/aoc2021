#include <iostream>
#include <queue>

using namespace std;

int main() {
    const int WINDOW = 3;
    int cur = 0;
    int inc = 0;
    queue<int> q;
    
    while (cin >> cur) {
        q.push(cur);
        if (q.size() > WINDOW) {
            if (q.front() < cur) inc++;
            q.pop();
        }
    }

    cout << inc << endl;
    
    return 0;
}
