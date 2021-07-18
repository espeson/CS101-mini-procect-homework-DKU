class node():
    def __init__(self, data):
        self.data = data
        self.next = None


class sorted_linked_list():
    def __init__(self):
        self.head = None

    def search(self, val):
        cul_node = self.head
        while cul_node != None:
            if str(cul_node.data) == str(val):
                return True
            cul_node = cul_node.next
        return False

    def __str__(self):
        if self.head == None:
            return ""
        a = str(self.head.data)
        cul_node = self.head
        while cul_node != None:
            cul_node = cul_node.next
            if cul_node == None:
                break
            a += ("->" + str(cul_node.data))
        return str(a)

    def remove(self, val):
        pre_node = None
        cul_node = self.head
        if val != self.head.data:
            while cul_node.next != None:
                pre_node = cul_node
                cul_node = cul_node.next
                if cul_node.data == node(val).data:
                    pre_node.next = cul_node.next
        if val == self.head.data:
            self.head = cul_node.next

    def insert(self, val):
        cur_node=self.head
        temp1=node(val)
        if cur_node==None:
            self.head=temp1
        if cur_node!=None:
            while val>cur_node.data:
                temp=cur_node.next
                if temp!=None:
                    if temp.data>=val:
                        cur_node.next=temp1
                        temp1.next=temp
                        break
                else:
                    cur_node.next=temp1
                    break
                cur_node=cur_node.next
            if val<cur_node.data:
                temp1.next=cur_node
                self.head=temp1

SLL = sorted_linked_list()

SLL.insert(2)
print(str(SLL) == '2')
SLL.insert(7)
print(str(SLL) == '2->7')
SLL.insert(3)
print(str(SLL) == '2->3->7')
