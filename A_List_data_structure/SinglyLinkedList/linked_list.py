from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def addToHead(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addToTail(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def addAfter(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node


    def addBefore(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.addAfter(prev_node, new_node)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def delete(self, node):
        prev_node = self.get_prev_node(node)
        #delete from head
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    def max(self):
        if self.head is None:
            return None
        max_value = self.head.data
        current = self.head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def min(self):
        if self.head is None:
            return None
        min_value = self.head.data
        current = self.head.next
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

    def count(self):
        c = 0
        current = self.head
        while current:
            c += 1
            current = current.next
        return c

    #______________________________________________________
    def get_mid(self, head): #using to detect the cycle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next # to check the middle node
        return slow

    def merge(self, left, right):
        dummy = Node(0)
        current = dummy

        while left and right:
            if left.data < right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        if left:
            current.next = left
        else:
            current.next = right
        return dummy.next

    def merge_sort(self, head): #using merge_sort
        if not head or not head.next:
            return head

        #Split the linked list into two halves
        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None

        #Recursively sort each half
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        # Merge the sorted halves
        sorted_list = self.merge(left, right)
        return sorted_list

    def sort(self):
        self.head = self.merge_sort(self.head)

    # ____________________________________________________________

    def bubbleSort(self):
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    swapped = True
                    current.data, current.next.data = current.next.data, current.data
                current = current.next

    def printArr(arr, n):
        i = 0
        while (i < n):
            print(arr[i], end = " ")
            i += 1
    # Function to return the length
    # of the Linked List
    def findlength(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    # Function to convert the Linked List to an array
    def convertArr(self):
        # Find the length of the
        # given linked list
        length = self.findlength()

        # Create an array of the
        # required length
        arr = []
        index = 0
        current = self.head
        # Traverse the Linked List and add the
        # elements to the array one by one
        while current is not None:
            arr.append(current.data)
            current = current.next
        # Print the created array
        self.printArr(arr, length)





















