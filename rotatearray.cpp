//leetcode Rotate Array 189 Medium challenge
//https://leetcode.com/problems/rotate-array/

#include <vector>

using namespace std;

class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        int n = nums.size();
        vector<int> copy = nums;
        for (int i = 0; i < n; i++)
        {
            nums[(i + k) % n] = copy[i];
        }
    }
}; 