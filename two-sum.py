class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        """

        """
            Solution:
                - Loop over the array. # num in nums
                - Check if the there is an h(num)
                    - If yes then return [index, h(num)]
                    - If no, add h(target - num) = index


        """

        dictionary = {};


        for index, num in enumerate(nums):
            value = target - num
            if(dictionary.get(num) is None):
                dictionary[value] = index
            else:  
                answer = []

                answer.append(dictionary[num])
                answer.append(index)
        
        return answer;
        
sol = Solution();

answer = sol.twoSum([1,22,3,1,5,9,62,74,8,11], 10);

print(answer)