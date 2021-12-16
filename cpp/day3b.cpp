#include <iostream>
#include <bitset>
#include <list>
#include <cstdlib>  // for abs

using namespace std;

const int MAXLEN = 12;

bitset<MAXLEN> filter(int nbits, list<bitset<MAXLEN>> nums, bool mode) {
    for (int pos = nbits-1; pos >= 0; pos--) {
        int count = 0;
        float thresh = nums.size()/2.0;

        for (auto it: nums)
            count += it[pos];

        bool match = count >= thresh ? mode : !mode;
        cerr << "pos:" << pos << "\t" << count << "<>"
             << thresh << "\t" << "match:" << match << endl;

        for (auto it = nums.begin(); it != nums.end();) {
            if ((*it)[pos] != match)
                it = nums.erase(it);
            else
                it++;
        }

        for (auto it: nums) {
            cerr << it << " ";
        } cerr << endl;

        if (nums.size() == 1)
            return nums.front();
    }
    return bitset<MAXLEN>(0);  // should never reach here
}

int main() {
    string binnum;
    list<bitset<MAXLEN>> nums;
    int nbits = 0;

    while (cin >> binnum)
        nums.emplace_back(binnum);
    nbits = binnum.length();

    bitset<MAXLEN> oxygen, co2;
    oxygen = filter(nbits, nums, 1);
    co2 = filter(nbits, nums, 0);
    cerr << "oxygen:" << oxygen << endl;
    cerr << "co2:" << co2 << endl;

    int doxygen = static_cast<int>(oxygen.to_ulong());
    int dco2 = static_cast<int>(co2.to_ulong());
    cout << doxygen * dco2 << endl;

    return 0;
}

