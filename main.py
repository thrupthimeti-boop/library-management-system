import csv

print("================================")
print("Library Management System")
print("================================")

while True:
    print("\nMenu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        with open("books.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([book_id, book_name, author])

        print("Book added successfully!")

    elif choice == "2":
        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)

                print("\nLibrary Books")
                print("------------------------------")

                for row in reader:
                    print("Book ID:", row[0])
                    print("Book Name:", row[1])
                    print("Author:", row[2])
                    print("------------------------------")

        except FileNotFoundError:
            print("No books found.")

    elif choice == "3":
        search_id = input("Enter Book ID to search: ")
        found = False

        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row and row[0] == search_id:
                        print("\nBook Found")
                        print("Book ID:", row[0])
                        print("Book Name:", row[1])
                        print("Author:", row[2])
                        found = True
                        break

            if not found:
                print("Book not found.")

        except FileNotFoundError:
            print("No books found.")

    elif choice == "4":
        update_id = input("Enter Book ID to update: ")
        updated_rows = []
        found = False

        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row and row[0] == update_id:
                        new_name = input("Enter New Book Name: ")
                        new_author = input("Enter New Author Name: ")
                        updated_rows.append([update_id, new_name, new_author])
                        found = True
                    else:
                        updated_rows.append(row)

            with open("books.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if found:
                print("Book updated successfully!")
            else:
                print("Book not found.")

        except FileNotFoundError:
            print("No books found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
