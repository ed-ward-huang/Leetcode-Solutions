class TreeNode:
    def __init__(self):
        self.nextLetter = {}
        self.terminate = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.nextLetter.keys():
                node.nextLetter[c] = TreeNode()
            node = node.nextLetter[c]

        node.terminate = True


    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.nextLetter.keys():
                return False
            node = node.nextLetter[c]
        
        if node.terminate:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.nextLetter.keys():
                return False
            node = node.nextLetter[c]
        
        return True
        
        