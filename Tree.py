class Tree:

    def compare(self, el1, el2, reverse = False):

        if(el1 > el2):
            reverse = not reverse
        return reverse

    def __init__(self, key):
        self.l = 0
        self.r = 0
        self.key = key

    def get_key(self):
        return self.key



    def insert(self, n_tree, reverse):
        """insert (добавление нового поддерева (ключа))
    сравнить ключ добавляемого поддерева (key) с ключом корневого узла (self.key).
    Если key>=self.key, рекурсивно добавить новое дерево в правое поддерево.
    Если key<self.key, рекурсивно добавить новое дерево в левое поддерево.
    Если поддерева нет, то вставить на это место новое дерево"""
        i = 1
        if(self.compare(self.key, n_tree.get_key(), reverse)):
            if(self.l != 0):
                i += self.l.insert(n_tree, reverse)
            else:
                self.l = n_tree
        else:
            if (self.r != 0):
                i += self.r.insert(n_tree, reverse)
            else:
                self.r = n_tree
        return i

    def traverse(self, clist):
        if(self.l != 0):
            self.l.traverse(clist)

        clist.append(self.key)

        if (self.r != 0):
            self.r.traverse(clist)








