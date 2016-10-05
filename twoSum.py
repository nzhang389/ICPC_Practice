class Solution(object):
    def twoSum(self, nums, target):
    	for indexFirst, valFirst in enumerate(nums)
    		for indexSecond in range(indexFirst, len(nums))
    			if(valFirst + nums[indexSecond])
    				return [indexFirst, indexSecond]



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def appendList(curList, remainingList, remainder):
    while remainder != 0:
        if remainingList: 
            curList = remainingList
            curList.val = curList.val + 1
            curList.val = curList.val % 10
            remainder = curList.val / 10
            curList = curList.next
            remainingList = remainingList.next
    curList = remainingList
    return remainder
        
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = l1
        remainder = 0
        val = 0
        while l3 and l2:
            # if l3 and l2:
            val = l3.val + l2.val + remainder
            # elif l3:
            #     val = l3.val + remainder
            # else:
                # l3.next = l2.next
                # val = l2.val + remainder
            remainder = val / 10
            l3.val = val % 10
            l3 = l3.next
            l2 = l2.next
        if l2:
            remainder = appendList(l3, l2, remainder)
        elif l3:
            remainder = appendList(l3, l3, remainder)
        if remainder == 1:
            l3 = ListNode(1)
        return l1
    

        