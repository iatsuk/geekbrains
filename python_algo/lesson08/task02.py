# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node[\'{self.left}\' : \'{self.right}\']'


class Tree:
    def __init__(self, node):
        self.root = node

    def __repr__(self):
        return f'Tree[{self.root}]'


def huffman_zip(s):
    def tree_traversal(structure, table, code):
        if isinstance(structure, Tree):
            tree_traversal(structure.root, table, code + "")
        elif isinstance(structure , Node):
            tree_traversal(structure.left, table, code + "0")
            tree_traversal(structure.right, table, code + "1")
        else:
            table[structure] = code

    # Входные данные
    c = Counter(s)
    # Строим дерево Хаффмана
    while len(c) > 1:
        elems = c.most_common()[:-3:-1]
        new_node = Node("", elems[1][0], elems[0][0])
        c.pop(elems[1][0])
        c.pop(elems[0][0])
        c[new_node] = elems[1][1] + elems[0][1]
    tree = Tree(c.popitem()[0])
    # Выводим таблицу Хаффмана
    huffman_table = dict()
    tree_traversal(tree, huffman_table, "")
    # Выводим закодированную строку
    result = [huffman_table[x] for x in s]
    return result


if __name__ == '__main__':
    print(huffman_zip('beep boop beer!'))
    print(huffman_zip('Алексей Петренко, спасибо за курс!'))
