import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    avl_set = SetAvl()

    out = []

    idx = 1
    for _ in range(N):
        command = input_data[idx]
        if command == "contains":
            val = int(input_data[idx + 1])
            idx += 2
            out.append("true" if avl_set.contains(val) else "false")

        elif command == "insert":
            val = int(input_data[idx + 1])
            idx += 2
            avl_set.insert(val)

        elif command == "remove":
            val = int(input_data[idx + 1])
            idx += 2
            avl_set.remove(val)

        elif command == "size":
            idx += 1
            out.append(str(avl_set.size()))

    sys.stdout.write("\n".join(out) + "\n")


class Node:
    __slots__ = ["value", "left", "right", "height"]

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class SetAvl:
    def __init__(self):
        self.root = None
        self._size = 0
        self._action_successful = False

    def size(self):
        return self._size

    def contains(self, x):
        curr = self.root
        while curr:
            if curr.value == x:
                return True
            elif x < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def insert(self, x):
        self._action_successful = False
        self.root = self._insert_node(self.root, x)
        if self._action_successful:
            self._size += 1

    def remove(self, x):
        self._action_successful = False
        self.root = self._remove_node(self.root, x)
        if self._action_successful:
            self._size -= 1

    def _right_rotation(self, root):
        pivot = root.left
        root.left = pivot.right
        pivot.right = root

        # Update root height
        rl_h = root.left.height if root.left else 0
        rr_h = root.right.height if root.right else 0
        root.height = 1 + (rl_h if rl_h > rr_h else rr_h)

        # Update pivot height
        pl_h = pivot.left.height if pivot.left else 0
        pivot.height = 1 + (pl_h if pl_h > root.height else root.height)

        return pivot

    def _left_rotation(self, root):
        pivot = root.right
        root.right = pivot.left
        pivot.left = root

        # Update root height
        rl_h = root.left.height if root.left else 0
        rr_h = root.right.height if root.right else 0
        root.height = 1 + (rl_h if rl_h > rr_h else rr_h)

        # Update pivot height
        pr_h = pivot.right.height if pivot.right else 0
        pivot.height = 1 + (pr_h if pr_h > root.height else root.height)

        return pivot

    def _insert_node(self, node, value):
        if not node:
            self._action_successful = True
            return Node(value)

        if value < node.value:
            node.left = self._insert_node(node.left, value)
        elif value > node.value:
            node.right = self._insert_node(node.right, value)
        else:
            return node

        lh = node.left.height if node.left else 0
        rh = node.right.height if node.right else 0
        node.height = 1 + (lh if lh > rh else rh)

        balance = lh - rh

        if balance > 1:
            if value < node.left.value:  # LL
                return self._right_rotation(node)
            else:  # LR
                node.left = self._left_rotation(node.left)
                return self._right_rotation(node)

        if balance < -1:
            if value > node.right.value:  # RR
                return self._left_rotation(node)
            else:  # RL
                node.right = self._right_rotation(node.right)
                return self._left_rotation(node)

        return node

    def _remove_node(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._remove_node(node.left, value)
        elif value > node.value:
            node.right = self._remove_node(node.right, value)
        else:
            self._action_successful = True

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            temp = node.right
            while temp.left is not None:
                temp = temp.left

            node.value = temp.value
            node.right = self._remove_node(node.right, temp.value)

        lh = node.left.height if node.left else 0
        rh = node.right.height if node.right else 0
        node.height = 1 + (lh if lh > rh else rh)

        balance = lh - rh

        if balance > 1:
            ll_h = node.left.left.height if node.left.left else 0
            lr_h = node.left.right.height if node.left.right else 0
            if ll_h >= lr_h:  # LL
                return self._right_rotation(node)
            else:  # LR
                node.left = self._left_rotation(node.left)
                return self._right_rotation(node)

        if balance < -1:
            rl_h = node.right.left.height if node.right.left else 0
            rr_h = node.right.right.height if node.right.right else 0
            if rr_h >= rl_h:  # RR
                return self._left_rotation(node)
            else:  # RL
                node.right = self._right_rotation(node.right)
                return self._left_rotation(node)

        return node


if __name__ == "__main__":
    main()
