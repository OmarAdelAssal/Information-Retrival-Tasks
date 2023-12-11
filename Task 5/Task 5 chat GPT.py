from binarytree import build, Node

# create a list of integers
input_values = [5, 3, 8, 1, 4, 6, 9]

# build a binary tree from the list
root = build(input_values)

# print the binary tree
print("The initial binary tree is:")
print(root)

# ask the user for input
while True:
    choice = input("Enter 1 to add a new element or 2 to delete an existing element: ")
    if choice == "1":

        input_value = int(input("Enter the input_value of the new element: "))
        new_node = root

        while new_node is not None:
            # if the input val smaller than root input_value
            if input_value < new_node.value:
                
                if new_node.left is None:
                    new_node.left = Node(input_value)
                    break
                else:
                    new_node = new_node.left

            else:
                if new_node.right is None:
                    new_node.right = Node(input_value)
                    break

                else:
                    new_node = new_node.right
        print("The updated binary tree is:")
        print(root)


    elif choice == "2":
        input_value = int(input("Enter the input_value of the element to be deleted: "))
        node_to_delete = None
        temp_node = root
        # this loop to determine which node to delete
        while temp_node is not None:
            if input_value == temp_node.value:
                node_to_delete = temp_node
                break
            elif input_value < temp_node.value:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right
        if node_to_delete is None:
            print("Element not found in the binary tree.")
        else:

            if node_to_delete.left is None and node_to_delete.right is None:
                if node_to_delete is root:
                    root = None

                elif node_to_delete is node_to_delete.parent.left:
                    node_to_delete.parent.left = None

                else:
                    node_to_delete.parent.right = None

                    
            elif node_to_delete.left is None and node_to_delete.right is not None:
                if node_to_delete is root:
                    root = node_to_delete.right

                elif node_to_delete is node_to_delete.parent.left:
                    node_to_delete.parent.left = node_to_delete.right

                else:
                    node_to_delete.parent.right = node_to_delete.right

                node_to_delete.right.parent = node_to_delete.parent
            elif node_to_delete.left is not None and node_to_delete.right is None:
                if node_to_delete is root:
                    root = node_to_delete.left
                elif node_to_delete is node_to_delete.parent.left:
                    node_to_delete.parent.left = node_to_delete.left
                else:
                    node_to_delete.parent.right = node_to_delete.left
                node_to_delete.left.parent = node_to_delete.parent
            else:
                successor = node_to_delete.right
                while successor.left is not None:
                    successor = successor.left
                node_to_delete.value = successor.value
                if successor is successor.parent.left:
                    successor.parent.left = successor.right
                else:
                    successor.parent.right = successor.right
                if successor.right is not None:
                    successor.right.parent = successor.parent
            print("The updated binary tree is:")
            print(root)
    else:
        print("Invalid input. Please enter 1 or 2.")