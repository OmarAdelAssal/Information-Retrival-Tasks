from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer,SnowballStemmer

inp_text = input("\nEnter Your Text Here : ")

print("______________________________________")

print("\nChoices:")
print('1: print tokenized words')
print('2: print tokenized sentences')
print('3: print original text')
print('4: Stemming')

print("\nChoose one of the above choices")

choice = int(input("Enter The Number of your choice: ")) 

print("______________________________________\n")

ps = PorterStemmer()
ss = SnowballStemmer("english")


if choice == 1:
    print(word_tokenize(inp_text))

elif choice == 2:
    print(sent_tokenize(inp_text))

elif choice == 3:
    print(inp_text)

elif choice == 4:
    print("1: porter Stemmer")
    print("2: Snowball Stemmer")
    print("Choose one of the above Choices")
    stem_choice = int(input("Enter The Number Of Your Choice: "))
    if stem_choice == 1:
        print(ps.stem(inp_text))
    elif stem_choice == 2 :
        print(ss.stem(inp_text))
    else:
        print("choose one of the available choices..!!!")
else:
    print("choose one of the available choices..!!!")


# Text for testing :
# Mohamed Salah Liverpool. Don't try this at home. The LCD monitor i bought last week is smart. I heared that there is a lion escape from The Zoo.

