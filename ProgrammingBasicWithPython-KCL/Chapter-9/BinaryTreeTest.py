from binaryTree import BinaryTree
root = BinaryTree('a')
print(root)
print(root.get_root_val())
print(root.get_left_child())
root.insert_left('b')
print(root.get_left_child().get_root_val())
root.insert_right('c')
print(root.get_right_child().get_root_val())
root.get_right_child().set_root_val('hello')
print(root.get_right_child().get_root_val())
root.insert_left('d')
print(root.get_left_child())
print(root.get_left_child().get_left_child().get_root_val())
