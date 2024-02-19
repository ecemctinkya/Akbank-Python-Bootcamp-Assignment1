class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  
        lines = self.file.readlines()
        for line in lines:
            book_info = line.strip().split(',')
            print(f"Book Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        lines = self.file.readlines()
        self.file.seek(0)
        updated_lines = [line for line in lines if title not in line]
        if len(lines) == len(updated_lines):
                print(f"Book '{title}' not found.")
        self.file.truncate(0)
        self.file.writelines(updated_lines)
        print(f"Book '{title}' removed successfully.")



lib = Library("books.txt")

while True:
    print("\n**** MENU ****")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")


    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

   

