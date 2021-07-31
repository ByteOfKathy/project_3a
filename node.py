class Node:

    def __init__(self, product, energy, fat, carbs, proteins, ingredients, left = None, right = None, parent = None):
        """
        args: product, energy, fat, carbs, proteins, ingredients, left, right, parent

        creates a Node
        """
        self.left = left
        self.right = right
        self.parent = parent

        self.__product = product
        self.__energy = energy
        self.__fat = fat
        self.__carbs = carbs
        self.__proteins = proteins
        self.__ingredients = ingredients

    def getProduct(self) -> str:
        return self.__product

    def getEnergy(self) -> int:
        return self.__energy
    
    def getFat(self) -> float:
        return self.__fat

    def getCarbs(self) -> float:
        return self.__carbs

    def getProteins(self) -> float:
        return self.__proteins

    def getIngredients(self) -> str: # may change to list
        return self.__ingredients

    def __str__(self) -> str:
        return "name: {}\nenergy: {}\nfat: {}\ncarbohydrates: {}\nproteins: {}\ningredients: {}\n".format(
            self.getProduct(), 
            self.getEnergy(), 
            self.getFat(), 
            self.getCarbs(), 
            self.getProteins(), 
            self.getIngredients()
        )

# lambda functions are fun...
# just does a comparison between a and b and returns the bigger one
comparison = lambda a, b: a if a > b else b

# are all these functions redundant? probably...
# but please don't go breaking my code and heart
# by using a comparison function other than these in BST.py
def productComparison(Node1, Node2) -> Node:
    """
    Sort by product

    Node1: first Node
    Node2: second Node

    returns larger product
    """ 
    return comparison(Node1.getProduct(), Node2.getProduct())

def energyComparison(Node1, Node2) -> Node:
    """
    Sort by energy

    Node1: first Node
    Node2: second Node

    returns larger energy
    """ 
    return comparison(Node1.getEnergy(), Node2.getEnergy())

def fatComparison(Node1, Node2) -> Node:
    """
    Sort by Fat

    Node1: first Node
    Node2: second Node

    returns larger Fat
    """ 
    return comparison(Node1.getFat(), Node2.getFat())

def carbsComparison(Node1, Node2) -> Node:
    """
    Sort by Carbs

    Node1: first Node
    Node2: second Node

    returns larger Carbs
    """ 
    return comparison(Node1.getCarbs(), Node2.getCarbs())

def proteinComparison(Node1, Node2) -> Node:
    """
    Sort by proteins

    Node1: first Node
    Node2: second Node

    returns larger Proteins
    """ 
    return comparison(Node1.getProteins(), Node2.getProteins())

def isSame(Node1, Node2) -> bool:
    """
    compares Nodes

    returns true if Nodes are at least a deep copy false otherwise
    """
    productSame = Node1.getProduct() == Node2.getProduct()
    energySame = Node1.getEnergy() == Node2.getEnergy()
    fatSame = Node1.getFat() == Node2.getFat()
    carbsSame = Node1.getCarbs() == Node2.getCarbs()
    proteinsSame = Node1.getProteins() == Node2.getProteins()
    ingredientsSame = Node1.getIngredients() == Node2.getIngredients()

    return productSame and energySame and fatSame and carbsSame and proteinsSame