
from nltk.tokenize import word_tokenize

inp_Word = input("Enter Word: ")
inverted_index = []

for i in range(1, 5):
    file = open(rf"Your Path\{i}.txt", "r")
    file_data = file.read()
    tokenized_list = word_tokenize(file_data)
    if inp_Word in tokenized_list:
        inverted_index.append(i)

print(inverted_index)
