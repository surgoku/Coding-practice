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
    
    def in_trie(self, trie, word):
        current_dict = trie
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
            
        if "_leaf_" in current_dict:
            return True
        else:
            return False
    
    
    def main(self):
        trie = self.make_trie('foo', 'bar', 'baz', 'barz')
        word = 'baz'
        self.in_trie(trie, word)
        
        
        
trie = Trie()

print trie.main()