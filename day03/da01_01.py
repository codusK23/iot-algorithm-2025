memory = []
head, curr, prev = None, None, None
dataArray = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end='')
    while current.link != None:
        current = current.link
        print(current.data, end='')
    print()

def makeSimpleLinkedList(namePhone):
    global memory, head, prev, curr
    printNodes(head)

    node = Node()
    node.data = namePhone
    memory.append(node)
    if head == None:
        head = node
        return
    if head.data[0] > namePhone[0]:
        node.link = head
        head = node
        return
    
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data[0] > namePhone[0]:
            prev.link = node
            node.link = curr
            return

    curr.link = node


if __name__ == '__main__':
    for data in dataArray:
        makeSimpleLinkedList(data)

    printNodes(head)