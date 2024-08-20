#include <vector>
#include <cmath>

// leetcode 1870 Medium challenge
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
// Writeup: https://hostileninja72.github.io/minspeed/

using namespace std;

class Solution
{
public:
    bool canReachInTime(const vector<int> &dist, double hour, int speed)
    {
        double time = 0;
        for (size_t i = 0; i < dist.size() - 1; ++i)
            time += ceil(static_cast<double>(dist[i]) / speed);

        time += static_cast<double>(dist.back()) / speed;
        return time <= hour;
    }

    int minSpeedOnTime(vector<int> &dist, double hour)
    {
        int low = 1, high = 1e7;
        while (low < high)
        {
            int mid = low + (high - low) / 2;
            if (canReachInTime(dist, hour, mid))
                high = mid;
            else
                low = mid + 1;
        }
        return canReachInTime(dist, hour, low) ? low : -1;
    }
};