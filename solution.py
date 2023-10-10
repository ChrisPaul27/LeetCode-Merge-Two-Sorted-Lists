class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
                return None
        elif list1 == None and list2 != None:
                return list2
        elif list1 != None and list2 == None:
            return list1
        dummy = None
        curr = None
        if list1.val < list2.val:
            curr = ListNode(list1.val, list1.next)
            dummy = ListNode(0, curr)
            list1 = list1.next
        else:
            curr = ListNode(list2.val, list2.next)
            dummy = ListNode(0, curr)
            list2 = list2.next
        
        
        while list1 != None:
            
            while list2 != None:
                
                if list2.val < list1.val:
                    curr.next = list2
                    curr = curr.next
                    #tmp = list2.next
                else:
                    curr.next = list1
                    curr = curr.next
                    break
                
                list2 = list2.next
            #list2 = tmp
            if list2 == None:
                curr.next = list1
                break
            list1 = list1.next
        
        if list2 != None:
            curr.next = list2        
        return dummy.next
