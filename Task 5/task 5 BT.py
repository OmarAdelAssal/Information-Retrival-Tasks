from binarytree import build

given_list = [1,2,3,4,5]

root = build(given_list)

print("Here is Our Tree That build from given list")
print(root)

while True:

    print("Choices:")
    print("1: Add a new element to the binary tree.")
    print("2: Delete an element from the binary tree.")
    print("0: if you want to Exit")
    choice = int(input("Enter The Number Of Your Choice: "))

    if choice == 1:
        value = int(input("Enter The value of node you want to add: "))
        given_list.append(value)
        root = build(given_list)
        print(root)

    elif choice == 2:
        value = int(input("Enter The value of node you want to remove: "))
        given_list.remove(value) 
        root = build(given_list)
        print(root)

    elif choice == 0:
        break

    else : 
        print("Please Enter One Of The Given Choices (0_0)")
