class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        vector<vector<int>> nums = customers;

        long long current_time = nums[0][0];
        long long avg = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (current_time < nums[i][0]) {
                current_time = nums[i][0];
            }

            current_time += nums[i][1];
            avg += current_time - nums[i][0];
        }

        return (double)avg / nums.size();
    }
};