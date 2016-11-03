class Trie:
    
    def __init__(self):
        self.tree = dict()

    def make_trie(self, *words):
        for word in words:
            current = self.tree
            for letter in word:
                current = current.setdefault(letter, {})

            current['leaf'] = '_leaf_'
            
        return self.tree
    
    
    def main(self):
        return self.make_trie('foo', 'bar', 'baz', 'barz')
        
        
        
trie = Trie()

print trie.main()