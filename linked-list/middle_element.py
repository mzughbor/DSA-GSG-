# Find the Middle of a Linked List Use slow and fast pointer approach.
# this way by fast, the other one is simple like getting length of the LL
# then //2 and while again until reaching that index and return- ofCourse it's
# taking much time, than the fast approach.

import time
from reverseSLL import SLL

class SLLME(SLL):
    
    @property
    def findMiddle(self):
        
        time_before = time.time()
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        time_after = time.time()
        print(f"{time_after - time_before:.10f} seconds")

        return slow.data

m = SLLME()
m.add_to_front(3).add_to_front(2).add_to_front(1).retrieve
print(m.findMiddle)