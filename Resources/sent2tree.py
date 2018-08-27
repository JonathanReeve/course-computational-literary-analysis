import ete3
from ete3 import Tree, TreeStyle, TextFace, add_face_to_node

class sentenceTree(): 
    def __init__(self, sent): 
        """ Takes a SpaCy sentence as input. """ 
        self.sent = sent
        self.root = sent.root
        print(self.sent)
        self.sentDict = self.sentToDict(self.root)
        self.newick = self.newickify(self.sentDict) + ';'

    def isPunct(self, thing): 
        if type(thing) == str: 
            if thing.strip() in "!@#$%^&*()_+-=,./<>?;':[]\{}|`~": 
                return True
        return False

    def sentToDict(self, node): 
        children = [child for child in node.children 
                   if self.isPunct(child.string.strip()) == False # ignore punctuation
                   and child.tag_ != 'SP'] #ignore spaces and newlines
        root = node.string.strip()
        if len(children) == 0: 
            return node.string.strip()
        return {node.string.strip(): [self.sentToDict(child) 
                                      for child in children]}

    def newickify(self, node): 
        if type(node) == str:
            return node.strip()
        root = list(node)[0]
        return '(' + ','.join([self.newickify(child) 
            for child in node[root] ]) + ')' + root
    
    def render(self, textMode=False): 
        """ 
        textMode=False will show a graphical tree. 
        textmode=True will show an ASCII tree. 
        """
        t = Tree(self.newick, format=1)
        if textMode: 
            print(t.get_ascii(show_internal=True))
        else: 
            ts = TreeStyle()
            ts.show_leaf_name = False
            #TODO: make this not be a function
            def my_layout(node):
                F = TextFace(node.name, tight_text=False)
                add_face_to_node(F, node, column=0, position="branch-right")
            ts.layout_fn = my_layout        
            return t.render('%%inline', tree_style=ts)

