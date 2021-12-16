#include <iostream>
#include <bitset>
#include <vector>

using namespace std;

const int MAXLEN = 12;

int main() {
    string binnum;
    vector<bitset<MAXLEN>> nums;
    int nbits = 0, nnums = 0;

    while (cin >> binnum)
        nums.emplace_back(binnum);
    nbits = binnum.length();
    nnums = nums.size();

    bitset<MAXLEN> gamma, epsilon;
    for (int pos = 0; pos < nbits; pos++) {
        int count = 0;
        for (auto it: nums)
            count += it[pos];

        if (count > nnums/2)
            gamma.set(pos);
        else
            epsilon.set(pos);
    }
    cerr << "gamma:" << gamma << endl;
    cerr << "epsilon:" << epsilon << endl;

    int dgamma = static_cast<int>(gamma.to_ulong());
    int depsilon = static_cast<int>(epsilon.to_ulong());
    cout << dgamma * depsilon << endl;

    return 0;
}

