class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def put(self, word, value):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.end = True


class Homework(Trie):
    def __init__(self):
        super().__init__()

    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")

        count = 0

        def dfs(node, current_word):
            nonlocal count
            if node.end and current_word.endswith(pattern):
                count += 1
            for char, child_node in node.children.items():
                dfs(child_node, current_word + char)

        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")

        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return True


if __name__ == "__main__":
    trie = Homework()

    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    suffix_results = [
        ("e", trie.count_words_with_suffix("e")),
        ("ion", trie.count_words_with_suffix("ion")),
        ("a", trie.count_words_with_suffix("a")),
        ("at", trie.count_words_with_suffix("at")),
    ]

    print("Результати для суфіксів:")
    for pattern, count in suffix_results:
        print(f"Кількість слів, що закінчуються на '{pattern}': {count}")

    prefix_results = [
        ("app", trie.has_prefix("app")),
        ("bat", trie.has_prefix("bat")),
        ("ban", trie.has_prefix("ban")),
        ("ca", trie.has_prefix("ca")),
    ]

    print("\nРезультати для префіксів:")
    for prefix, exists in prefix_results:
        result = "Знайдено" if exists else "Не знайдено"
        print(f"Префікс '{prefix}': {result}")

    print("\nТести пройдено успішно!")
