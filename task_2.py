class Node:
    def __init__(self):
        self.children = {}  # Діти цього вузла
        self.end = False  # Позначає кінець слова


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
            return ""  # Якщо масив порожній, повертаємо порожній рядок

        # Додаємо всі слова в Trie
        for word in strings:
            self.put(word)

        # Тепер шукаємо найдовший спільний префікс
        prefix = ""
        current_node = self.root
        while current_node and len(current_node.children) == 1 and not current_node.end:
            # Вибираємо єдиного нащадка
            char, next_node = next(iter(current_node.children.items()))
            prefix += char
            current_node = next_node

        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(trie.find_longest_common_word(strings))  # Повинно вивести "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(trie.find_longest_common_word(strings))  # Повинно вивести "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(trie.find_longest_common_word(strings))  # Повинно вивести ""
