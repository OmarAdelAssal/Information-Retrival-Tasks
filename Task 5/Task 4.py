# old code 


# # m is the size of input list / number of all elements, v is the value
# def hash_key(v, m):
#     h_v = v % m
#     return h_v

# # print("hash key formula : h(v) = v % m")

# # m_inp = int(input("Enter m : m is the size of input list: "))
# # v_inp = int(input("Enter v : v is the value: "))

# # print(f"h({v_inp}) = {v_inp} % {m_inp} = {hash_key(v_inp,m_inp)}")
# # print("Hash Key: ",hash_key(v_inp,m_inp))


# ################################################################################



# def hash(arr):
#     Hash_dict = {}
#     for i in range(len(arr)):
#         myKey = hash_key(arr[i],len(arr))
#         Hash_dict[arr[i]] = myKey
#     return Hash_dict


# given_list = [3, 2, 9, 11, 7]

# hash_table = hash(given_list)
# # print("{value : hash key}")

# # print(hash_table)

# print("Choices:")
# print("1: Construct the whole hash table ")
# print("2: Add a new element to the hash table")
# print("3: Update a value of a certain key")
# print("4: Delete an element from the hash table")
# print("5: Search for an element in the hash table")
# print("6: print All elements with their keys of the hash table")

# choice = int(input("Enter The Number Of Your Choice: "))

# if choice == 1 :
#     print("{value : hash key}")
#     print(hash_table)


# elif choice == 2 :
#     new_elem_inp = int(input("Enter The New Element Value: "))
#     hash_table[new_elem_inp] = hash_key(new_elem_inp, len(given_list))
#     print(hash_table)


# elif choice == 3 :
#     certain_key = int(input("Enter the value of Key you want to Update "))
#     hash_table[certain_key] = hash_key(certain_key, len(given_list))
#     print(hash_table)
    

# elif choice == 4:
#     delet_element = int(input("Enter the value of the element you want to delete from hash table: "))
#     del hash_table[delet_element]
#     print(hash_table)


# elif choice == 5:
#     search_element = int(input("Enter the value of Element you want to search for : "))
#     if search_element in hash_table.keys():
#         print("Found")
    
#     else : print("Not Found")

# elif choice == 6:
#     print("{hash key : value}")
#     print(hash_table)

# else :
#     print(" Choice Not Found  (o_o) ")

##################################################################################

# new code 

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
    print("Choices:")
    print("1: Construct the whole hash table ")
    print("2: Add a new element to the hash table")
    print("3: Update a value of a certain key")
    print("4: Delete an element from the hash table")
    print("5: Search for an element in the hash table")
    print("6: print All elements with their keys of the hash table")
    print("7: Exit")

    choice = int(input("Enter The Number Of Your Choice: "))

    if choice == 1 :
        print("{hash key : value}")
        print(hash_table)


    elif choice == 2 :
        new_elem_inp = int(input("Enter The New Element Value: "))
        # appending new element to the given list to compute the hash key on the new length of list
        given_list.append(new_elem_inp)
        hash_table[hash_key(new_elem_inp, len(given_list))].append(new_elem_inp)
        print(hash_table)

    elif choice == 3 :
        certain_key = int(input("Enter the value of Key you want to Update "))
        if hash_key(certain_key, len(given_list)) in hash_table:
            hash_table[hash_key(certain_key, len(given_list))].remove(certain_key)
            hash_table[hash_key(certain_key, len(given_list))].append(int(input("Enter the new value for the key: ")))
            print(hash_table)
        else:
            print("Key not found in hash table.")

    elif choice == 4:
        delete_element = int(input("Enter the value of the element you want to delete from hash table: "))
        key = hash_key(delete_element, len(given_list))
        if key in hash_table:
            if delete_element in hash_table[key]:
                hash_table[key].remove(delete_element)
                print(hash_table)
            else:
                print("Element not found in hash table.")
        else:
            print("Key not found in hash table.")

    elif choice == 5:
        search_element = int(input("Enter the value of Element you want to search for : "))
        key = hash_key(search_element, len(given_list))
        if key in hash_table and search_element in hash_table[key]:
            print("Found")
        else:
            print("Not Found")

    elif choice == 6:
        print("{hash key : value}")
        print(hash_table)

    elif choice == 7:
        print("Exiting...")
        break

    else :
        print(" Choice Not Found  (o_o) ")