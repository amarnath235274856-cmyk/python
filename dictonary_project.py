dictionary={}
while True:
    print("add a word")
    print("search for meaning")
    print("display all words")
    print("update meaning")
    print("delete word")
    print("exit")
    choice=(input("enter the choice:"))


    if choice == "1":
      word=input("enter the word:").lower()
      meaning=input("enter the meaning")
      dictionary[word]=meaning
      print("successsful",word)

    elif choice=="2":
       word=input("enter the word").lower()
       if word in  dictionary:
          print("meaning",dictionary[word])
       else:
          print("word is not in dictionary")

    elif choice=="3":
       if dictionary:
          print("words and their meaning")
          for word ,meaning in dictionary.items():
             print(f"{word}:{meaning}")
          else:
             print("dictionary is empty")

    elif choice=="4":
       word=input("enter the word update meaning").lower()
       if word in dictionary:
         new_meaning=input("enter the new meaning")
         dictionary[word]=new_meaning
         print("update meaning")
         print("update meaning",dictionary[word])
       else:
          print("word not found in the dictionary")
    elif choice == "5":
        word = input("Enter the word to delete: ").lower()

        if word in dictionary:
            del dictionary[word]
            print(f"'{word}' has been deleted successfully.")
        else:
            print(f"'{word}' does not exist in the dictionary.")
    elif choice == "6":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 3.")
          