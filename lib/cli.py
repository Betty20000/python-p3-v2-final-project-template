from models.models import Category, Book

class CLI:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Update Categories")
            print("2. Update Books")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.category_menu()
            elif choice == '2':
                self.book_menu()
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def category_menu(self):
        while True:
            print("\nCategory Menu:")
            print("1. Create Category")
            print("2. Delete Category")
            print("3. View All Categories")
            print("4. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_category()
            elif choice == '2':
                self.delete_category()
            elif choice == '3':
                self.view_all_categories()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def book_menu(self):
        while True:
            print("\nBook Menu:")
            print("1. Create Book")
            print("2. Delete Book")
            print("3. View All Books")
            print("4. View Books by Book ID")
            print("5. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_book()
            elif choice == '2':
                self.delete_book()
            elif choice == '3':
                self.view_all_books()
            elif choice == '4':
                self.view_books_by_category()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def view_books_by_category(self):
        category_id = int(input("Enter category ID to view employees: "))

        books = Book.get_by_category_id(category_id)
        if books:
            print("\nBooks in Category {}:".format(category_id))
            for book in books:
                print(book)
        else:
            print("No books found in category {}.".format(category_id))

    def create_category(self):
        title = input("Enter category name: ")
        Category.create(title)
        print("Category created successfully.")

    def delete_category(self):
        category_id = int(input("Enter category ID to delete: "))
        Category.delete(category_id)
        print("Category deleted successfully.")

    def view_all_categories(self):
        categories = Category.get_all()
        if categories:
            print("\nAll Categories:")
            for category in categories:
                print(category)
        else:
            print("No categories found.")

    def create_book(self):
        title = input("Enter book name: ")
        author = (input("Enter book author: "))
        publishyear = float(input("Enter book year of publish: "))
        category_id = int(input("Enter book category ID: "))
        category_title = input("Enter book category: ")
        Book.create(title, author, publishyear, category_id, category_title)
        print("Book created successfully.")

    def delete_book(self):
        book_id = int(input("Enter book ID to delete: "))
        Book.delete(book_id)
        print("Book deleted successfully.")

    def view_all_books(self):
        books = Book.get_all()
        print("\n All Books:")
        for book in books:
            print(book)
        else:
            print("No books found.")

if __name__ == "__main__":
    cli = CLI()