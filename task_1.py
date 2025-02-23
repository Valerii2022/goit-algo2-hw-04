class Node:
    def __init__(self):
        self.children = {}  # Діти цього вузла
        self.end = False  # Позначає кінець слова


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
        # Перевірка на коректність введення
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")

        count = 0

        # Функція для пошуку слів, що закінчуються на pattern
        def dfs(node, current_word):
            nonlocal count
            if node.end and current_word.endswith(pattern):
                count += 1
            for char, child_node in node.children.items():
                dfs(child_node, current_word + char)

        # Починаємо пошук з кореня
        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        # Перевірка на коректність введення
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")

        current_node = self.root

        # Проходимо по кожному символу префікса
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return True


if __name__ == "__main__":
    trie = Homework()

    # Додавання слів до дерева
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    suffix_results = [
        ("e", trie.count_words_with_suffix("e")),  # apple
        ("ion", trie.count_words_with_suffix("ion")),  # application
        ("a", trie.count_words_with_suffix("a")),  # banana
        ("at", trie.count_words_with_suffix("at")),  # cat
    ]

    # Виведення результатів для суфіксів
    print("Результати для суфіксів:")
    for pattern, count in suffix_results:
        print(f"Кількість слів, що закінчуються на '{pattern}': {count}")

    # Перевірка наявності префікса
    prefix_results = [
        ("app", trie.has_prefix("app")),  # apple, application
        ("bat", trie.has_prefix("bat")),  # False
        ("ban", trie.has_prefix("ban")),  # banana
        ("ca", trie.has_prefix("ca")),  # cat
    ]

    # Виведення результатів для префіксів
    print("\nРезультати для префіксів:")
    for prefix, exists in prefix_results:
        result = "Знайдено" if exists else "Не знайдено"
        print(f"Префікс '{prefix}': {result}")

    print("\nТести пройдено успішно!")






