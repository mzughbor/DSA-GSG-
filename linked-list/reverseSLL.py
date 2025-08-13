
# practise some -
# Then do reverse idea for SLL, the duple one is easier, you know

""" 
current = head
while current:
    current.prev, current.next = current.next, current.prev
    current = current.prev  # because we swapped next & prev
head, tail = tail, head
 """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        current = self.head
        newNode = Node(data)
        self.head = newNode
        newNode.next = current
        return self

    # another way to print data, nice idea // no chaining 
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += f"[{temp.data}]->"
            temp = temp.next
        result += " None"
        return result

    @property
    def retrieve(self):
        current = self.head
        while current != None:
            print(current.data, end="-> ")
            current = current.next
        print("None", end="")
        print("\n")
        return self

    @property
    def reverse(self):
        current = self.head
        # I think the key from this is all about creating a hubothitacal prev to connect,
        # in order to solve, and flip prev with next | head with tail idea...
        # assume we have like this : "1 -> 2 -> 3 -> None"
        # after our assumpation le'ts have for 1 prev = None then use it to insert the chain...
        previous = None # on the previous i can now bind the list and move to get the rest 
        while current != None:
            nxt = current.next # it's important after it we have the rest of data, right!
            current.next = previous # the previous is Null 
            
            previous = current # what we forget / almost all the time..
            
            current = nxt # is the rest elements...
            # it's just an image from the real Next, that's it all, save it to get it back 
            # now we still missing one peace is the real new head
        if current is None:
            self.head = previous # latest node is the head now
            return self

    #method to compute the length or the depth of sll  // no chaining 
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp  = temp.next
        return count
    
    
    @property
    # delete from the end
    def delete_from_end(self):
        lenLL = self.length()

        if lenLL == 0:
            return self
        elif lenLL == 1:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        return self

    # delete at start
    @property
    def delete_at_start(self):
        if self.head is None:
            return self
        else:
            self.head = self.head.next
            return self

    #deleting between two nodes...
    def delete_at(self, index):
        
        current = self.head
        if current is None or index < 0:
            return self
        
        if index == 0:
            self.head = self.head.next
            return self
        
        counter = 0
        while (counter < index-1 and current.next is not None ):
            counter += 1
            current = current.next
        
        if current.next is not None:
            rest = current.next.next
            current.next = rest
        else:
            print("Sorry the index is wrong / didn't exist in SLL...")
        return self    

#test
t = SLL()
t.add_to_front(6).add_to_front(5).add_to_front(4).retrieve
t.add_to_front(3).add_to_front(2).add_to_front(1).retrieve
t.reverse.retrieve.add_to_front(7).retrieve
print("-----")
t.add_to_front("kk")
print(t.__str__())
print("-----")

# in case one element
m = SLL()
m.add_to_front("MMM").retrieve
m.delete_from_end.retrieve

print("-----")
# in case two element
mm = SLL()
mm.add_to_front("m").add_to_front("mm").retrieve.delete_from_end.retrieve

print("-----")
# in case three element
mm = SLL()
mm.add_to_front("m").add_to_front("mm").add_to_front("mmm").retrieve.delete_from_end.retrieve

print("Try deleteing from fisrt")
mm.delete_at_start.retrieve #.delete_at_start.retrieve

print("-----")
print("try deleting at spcifc index...")
K = SLL()
K.add_to_front("aya").add_to_front("ayat").add_to_front("ayman").add_to_front("ayham").retrieve
K.delete_at(2).retrieve

