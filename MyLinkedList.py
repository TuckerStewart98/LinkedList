# Linked List data structure.

# Node class to encapsulate data and chain them together.
class Node:
    # The data stored in the node.
    __myData = 0
    # A pointer to the next node in the sequence
    __myNext = None
    
    # Constructor for the node, wraps the data sent in.
    def __init__(self, data, nextNode):
        self.__myData = data
        self.__myNext = nextNode
    # Returns the data stored in the node.
    def getData(self):
        return self.__myData
        
    # Returns a pointer to the next node in the sequence.
    def getNext(self):
        return self.__myNext
        
    # Changes the point to the next node to the one in the parameters.
    def setNext(self, nextNode):
        self.__myNext = nextNode
        
    # Returns the string representation of the data inside.
    def toString(self):
        return "{}".format(self.__myData)
        
        
        
# The Linked List data Structure
class MyLinkedList:
    # First node in the sequence
    __myHeadNode = None
    # Last node in the sequence
    __myLastNode = None
    # Number of elements/nodes in this list.
    __mySize = 0
    
    # Default constructor for the Linked List.
    def __init__(self):
        self.__myHeadNode = None
        self.__myLastNode = None
        self.__mySize = 0
        
    # Returns the size of the Linked List.
    def size(self):
        return self.__mySize
        
    # Adds the data to the end of the Linked List.
    def add(self, data):
        newNode = Node(data, None)
        # If there are no nodes in the List create the first one.
        if self.__myHeadNode is None:
            self.__myHeadNode = newNode
            self.__myLastNode = newNode
        # Else append the new node to the end of the List.
        else:
            self.__myLastNode.setNext(newNode)
            self.__myLastNode = newNode
        # Increment size by one.
        self.__mySize += 1
    
    # Returns the data stored in the ith node. Raises an excpetion if the index
    # is out of bounds, less than zero or greater than or equal to the size.
    def get(self, index):
        # Raise exception if 
        if index >= self.__mySize or index < 0:
            raise Exception('OutOfBoundsException')
        
        dataNode = self.__myHeadNode
        for i in range(index):
            dataNode = dataNode.getNext()
        return dataNode.getData()

# Test the Linked List
list1 = MyLinkedList()
list1.add(1)
list1.add(5)
list1.add(-7)
for i in range(list1.size()):
    print(list1.get(i))
