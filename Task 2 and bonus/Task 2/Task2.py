from nltk.tokenize import word_tokenize, sent_tokenize

inp_text = input("\nEnter Your Text Here : ")

print("______________________________________")

print("\nChoices:")
print('1: print tokenized words')
print('2: print tokenized sentences')
print('3: print original text')

print("\nChoose one of the above choices")

choice = int(input("Enter The Number of your choice: ")) 

print("______________________________________")

print("\nResult : ")

if choice == 1:
    print(word_tokenize(inp_text))

elif choice == 2:
    print(sent_tokenize(inp_text))

else :
    print(inp_text)


# Text for testing :
# Mohamed Salah Liverpool. Don't try this at home. The LCD monitor i bought last week is smart. I heared that there is a lion escape from The Zoo.

