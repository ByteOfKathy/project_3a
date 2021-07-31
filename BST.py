import node

class BST:
    def __init__(self, root):
        self.__root = root

    def getRoot(self) -> node.Node:
        return self.__root

    def printPostOrder(self, n = None):
        """
        n: current node, default is root
        """

    # TODO
    def insertNode(self, n, comparisonFunction, tiebreakerFunction, root) -> node.Node:
        """ 
        inserts a new node

        n: node
        comparisonFunction: function to compare nodes by
        
        returns n
        """

        if self.__root is None:
            self.__root = n
            return n
        else:
            # if n is smaller
            if comparisonFunction(n, root) == root:
                if root.left is not None:
                    return insertNode(n, comparisonFunction, tiebreakerFunction, root.left)
                else:
                    root.left = n
                    n.parent = root
                    return n
            # if n is bigger, duplicates are not allowed in BST
            else if comparisonFunction(n, root) == n:
                if root.right is not None:
                    return insertNode(n, comparisonFunction, tiebreakerFunction, root.right)
                else:
                    root.right = n
                    n.parent = root
                    return n
            # TODO
            else: 
                # tiebreaker n is smaller
                if tiebreakerFunction(n, root) == root:
                
                else if tiebreakerFunction(n, root) == n:

                else:
                    throw ValueError("tie breaker function did not break tie")
                    