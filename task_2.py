class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def put(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.end = True


class LongestCommonWord(Trie):
    def __init__(self):
        super().__init__()

    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        for word in strings:
            self.put(word)

        prefix = ""
        current_node = self.root
        while current_node and len(current_node.children) == 1 and not current_node.end:
            char, next_node = next(iter(current_node.children.items()))
            prefix += char
            current_node = next_node

        return prefix


if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(trie.find_longest_common_word(strings))

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(trie.find_longest_common_word(strings))

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(trie.find_longest_common_word(strings))
