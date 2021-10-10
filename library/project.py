from virtual_library import *

menu = """
***********************************
WELCOME TO THE VIRTUAL LIBRARY    
***********************************
1. Show me the books
2. Query the books
3. Add a book
4. Delete a book
5. Back to menu

NOTE: 'q' for quit. 
***********************************
"""
print(menu)
library = Library()
while True:
    choice = input("What do you want to do?\n==>")
    if(choice == "q"):
        print("[*] Quitting...")
        time.sleep(1)
        break
    elif(choice == "1"):
        library.show_the_books()
    elif(choice == "2"):
        name = input("Which book do you want?\n==>")
        print("Searching for a book...")
        time.sleep(1)
        library.query_book(name)
    elif(choice == "3"):
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        category = input("Category:")
        page = input("Page:")
        new_book = Book(name, author, publisher, category, page)
        print("[*] Adding book...")
        library.add_book(new_book)
        time.sleep(2)
        print("[*] The book is added!")
    elif(choice == "4"):
        name = input("[*] Which book do you want to delete?\n==>")
        ans = input("[*] Are you sure you want to delete the book? (Yes/No):")
        if(ans == "Yes"):
            print("[*] The book is deleting...")
            library.delete_book(name)
            time.sleep(1)
            print("[*] The book has been deleted!")
        elif(ans == "No"):
            continue
        else:
            print("[*] Invalid choice!")
    elif (choice == "5"):
        print(menu)
    else:
        print("[*] Invalid choice!")
