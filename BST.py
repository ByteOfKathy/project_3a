import node

class BST:
    def __init__(self, root):
        self.__root = root

    def getRoot(self):
        return self.__root

    # TODO
    '''
    def insertNode(self, n, comparisonFunction) -> node:
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
    '''