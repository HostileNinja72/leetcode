//leetcode H-index 274 Medium challenge
//https://leetcode.com/problems/h-index/

#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int hIndex(vector<int> &citations)
    {
        int h;
        std::sort(citations.begin(), citations.end(), [](int a, int b)
             { return a > b; });
        for (h = 1; h <= citations.size() && citations[h - 1] >= h; h++)
        {
        }
        return h - 1;
    }
};
