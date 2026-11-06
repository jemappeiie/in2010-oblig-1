def main():
    N = int(input())
    avl_set = SetAvl()
    for _ in range(N):
        command = input().split()
        if command[0] == "contains":
            print(str(avl_set.contains(int(command[1]))).lower())

        if command[0] == "insert":
            avl_set.insert(int(command[1]))

        if command[0] == "remove":
            avl_set.remove(int(command[1]))

        if command[0] == "size":
            print(avl_set.size())


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class SetAvl:
    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        return self._size

    def contains(self, x):
        curr = self.root
        while curr:
            if curr.value == x:
                return True
            elif x < curr.value:  # Corrected: go left if x is smaller
                curr = curr.left
            else:  # Corrected: go right if x is larger
                curr = curr.right
        return False

    def insert(self, x):
        if not self.contains(x):
            # Corrected: must assign back to self.root
            self.root = self._insert_node(self.root, x)
            self._size += 1

    def remove(self, x):
        # Corrected: must only remove if it CONTAINS x
        if self.contains(x):
            # Corrected: must assign back to self.root
            self.root = self._remove_node(self.root, x)
            self._size -= 1

    # Private helper methods
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _right_rotation(self, root):
        pivot = root.left
        root.left = pivot.right
        pivot.right = root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        pivot.height = 1 + max(
            self._get_height(pivot.left), self._get_height(pivot.right)
        )

        return pivot

    def _left_rotation(self, root):
        pivot = root.right
        # Corrected: root takes pivot's left child, not pivot taking its own left child
        root.right = pivot.left
        pivot.left = root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        pivot.height = 1 + max(
            self._get_height(pivot.left), self._get_height(pivot.right)
        )

        return pivot

    def _insert_node(self, node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._insert_node(node.left, value)
        else:
            node.right = self._insert_node(node.right, value)

        # Corrected: properly calling self._get_height(node.right)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # LL
        if balance > 1 and value < node.left.value:
            return self._right_rotation(node)
        # RR
        if balance < -1 and value > node.right.value:
            return self._left_rotation(node)
        # LR
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotation(node.left)
            return self._right_rotation(node)
        # RL
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotation(node.right)
            return self._left_rotation(node)

        return node

    def _min_value_node(self, node):
        curr = node
        # Corrected: removed faulty if-condition that caused an infinite loop
        while curr.left is not None:
            curr = curr.left
        return curr

    def _remove_node(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._remove_node(node.left, value)
        elif value > node.value:
            node.right = self._remove_node(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._remove_node(node.right, temp.value)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Corrected: all rotations now use the exact method names _right_rotation and _left_rotation
        # LL
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotation(node)
        # RR
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotation(node)
        # LR
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotation(node.left)
            return self._right_rotation(node)
        # RL
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotation(node.right)
            return self._left_rotation(node)

        return node


if __name__ == "__main__":
    main()
