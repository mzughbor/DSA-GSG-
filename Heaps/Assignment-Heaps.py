class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i):
        max_index = i
        left = self._left_child(i)
        right = self._right_child(i)
        n = len(self.heap)

        if left < n and self.heap[left] > self.heap[max_index]:
            max_index = left
        if right < n and self.heap[right] > self.heap[max_index]:
            max_index = right

        if max_index != i:
            self._swap(i, max_index)
            self._heapify_down(max_index)

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0


# Test
if __name__ == "__main__":

    max_heap = MaxHeap()
    integers_to_insert = [5, 1, 3, 7, 1, 9, 5]

    print(f"Inserting integers: {integers_to_insert}")
    for num in integers_to_insert:
        max_heap.insert(num)
        print(f"Heap after inserting {num}: {max_heap.heap}")

    print("\nPopping elements in descending order:")
    while not max_heap.is_empty():
        popped_element = max_heap.pop()
        print(f"Popped: {popped_element}, Remaining Heap: {max_heap.heap}")