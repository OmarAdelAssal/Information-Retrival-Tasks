from collections import defaultdict

# m is the size of input list / number of all elements, v is the value
def hash_key(v, m):
    # h(v) = v % m
    h_v = v % m
    return h_v


def hash(arr):
    Hash_dict = defaultdict(list)
    for i in range(len(arr)):
        myKey = hash_key(arr[i],len(arr))
        Hash_dict[myKey].append(arr[i])
    return dict(Hash_dict)

given_list = [3, 2, 9, 11, 7]


hash_table = hash(given_list)


while True:

    print("\n-----------------------------")
    print("Choices:")
    print("1: Construct the whole hash table ")
    print("2: Add a new element to the hash table")
    print("3: Update a value of a certain key")
    print("4: Delete an element from the hash table")
    print("5: Search for an element in the hash table")
    print("6: print All elements with their keys of the hash table")
    print("7: Exit")
    
    choice = int(input("Enter The Number Of Your Choice: "))

    # constructing
    if choice == 1 :
        hash_table = hash(given_list)

    # Adding
    elif choice == 2 :
        new_elem_inp = int(input("Enter The New Element Value: "))
        # appending new element to the given list to compute the hash key on the new length of list
        given_list.append(new_elem_inp)
        hash_table[hash_key(new_elem_inp, len(given_list))].append(new_elem_inp)
        print(hash_table)

    # Updating
    elif choice == 3 :
        certain_key = int(input("Enter the value of Key you want to Update "))
        hash_table[hash_key(certain_key, len(given_list))] = certain_key
        print(hash_table)
        
    # Deleting
    elif choice == 4:
        delet_element = int(input("Enter the value of the element you want to delete from hash table: "))
        del hash_table[delet_element]
        print(hash_table)

    # Searching
    elif choice == 5:
        search_element = int(input("Enter the value of Element you want to search for : "))
        if search_element in hash_table.keys():
            print("Found")
        
        else : print("Not Found")

    # Printing
    elif choice == 6:
        print("{hash key : value}")
        print(hash_table)

    # Exiting
    elif choice == 7:
        break

    else :
        print(" Choice Not Found  (o_o) ")