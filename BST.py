import node
import queue

class BST:
    def __init__(self, root: node.Node = None, comparisonFunction = node.productComparison):
        self.__root = root
        self.__comparisonFunction = comparisonFunction

    def getRoot(self) -> node.Node:
        return self.__root

    def printInOrder(self, root: node.Node):
        """
        prints tree in order
        """
        
        if not root:
            return
        # queue
        q = queue.Queue()
        q.put(root)

        while q.qsize() > 0:
            height = q.qsize()
            while height > 0:
                temp = q.get()
                print(temp, end = "---------------\n")
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
                height -= 1

    # TODO In theory this works, but haven't tested it past 2 recursive calls...
    def insertNode(self, n: node.Node, root: node.Node) -> node.Node:
        """ 
        inserts node n using the passed comparison function
        
        returns n
        """

        # Assuming root that gets passed is not None
        if self.__root is None:
            self.__root = n
            return n
        else:
            # if n is smaller
            if self.__comparisonFunction(n, root) is root:
                # duplicates not allowed
                if node.isSame(root, n): 
                    # value error because duplicates aren't allowed FOR TESTING ONLY
                    raise ValueError
                    # return n

                if root.left is not None:
                    return self.insertNode(n, root.left)
                else:
                    root.left = n
                    n.parent = root
                    return n
            # if n is bigger
            elif self.__comparisonFunction(n, root) is n:
                if root.right is not None:
                    return self.insertNode(n, root.right)
                else:
                    root.right = n
                    n.parent = root
                    return n
    
    # TODO test this
    def searchNode(self, n: node.Node, root: node.Node):
        # value not found in tree or value found
        if self.__root is None or node.isSame(n, root):
            return root
        # n is bigger
        elif self.__comparisonFunction(root, n) is n and root.right is not None:
            return self.searchNode(n, root.right)
        # n is smaller
        elif self.__comparisonFunction(root, n) is root and root.left is not None:
            return self.searchNode(n, root.left)
        else: 
            return None