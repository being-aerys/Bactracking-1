# Created by Aashish Adhikari at 5:13 PM 1/26/2021

class Solution(object):


    def helper(self, candidates, target, index, curr_path):

        # base cases
        if target == 0:
            self.sol.append(copy.deepcopy(curr_path))

        elif target < 0:
            # do not further traverse
            pass

        elif index == len(candidates):



        # logic
        else:

            # left path : dont choose the element
            self.helper(candidates, target, index + 1, curr_path)

            # right path : choose the element
            curr_path.append(candidates[index])
            self.helper(candidates, target - candidates[index], index, curr_path)

            # after the right side finishes, remove the last element that was appended to as we need to return the execution to the upper level
            curr_path.pop()






    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []

        self.sol = []
        curr_path = []
        self.helper(candidates, target, 0, curr_path)

        return self.sol


        