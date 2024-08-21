// leetcode Best Time to Buy and Sell Stock II 122 Medium challenge
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

#include <vector>

using namespace std;

class Solution
{
public:
    int maxProfit(std::vector<int> &prices)
    {
        int maxProfit = 0;

        for (int i = 1; i < prices.size(); ++i)
        {
            int profit = prices[i] - prices[i - 1];
            if (profit > 0)
            {
                maxProfit += profit;
            }
        }

        return maxProfit;
    }
};