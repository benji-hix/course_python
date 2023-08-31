class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def remove_from_front(self):
        runner = self.head.next
        self.head = None
        self.head = runner
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_back(self):
        runner = self.head
        while (runner.next != None):
            if runner.next.next == None:
                runner.next = None
            else:
                runner = runner.next
        return self
        
    def insert_at_n(self, val, location):
        new_node = SLNode(val)
        runner_count = 1
        runner = self.head
        while runner_count < location - 1:
            runner = runner.next
            runner_count += 1
        temp = runner.next
        runner.next = new_node
        new_node.next = temp
        return self

    def remove_val(self, val):
        runner = self.head
        while (runner.next != None):
            if runner.next.value == val:
                runner.next = runner.next.next
                return self
            else:
                runner = runner.next

    def print_values(self):
        runner = self.head # points to list's first node
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_singly_linked_list = SList()

# ---------------- testing adding/removing from front and back --------------- #
# my_singly_linked_list.add_to_front('are').add_to_back('fun').add_to_front('linked lists').print_values()
# print("")
# my_singly_linked_list.remove_from_back().remove_from_front().print_values()

# ------------------- testing for middle insertion/removal ------------------- #
my_singly_linked_list.add_to_front('a').add_to_back('b').add_to_back('c').add_to_back('d').add_to_back('e').print_values()
print('')
my_singly_linked_list.insert_at_n('x', 3).print_values()
print('')
my_singly_linked_list.remove_val('c').print_values()