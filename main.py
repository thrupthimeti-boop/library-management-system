import csv

print("===================================")
print("Library Management System")
print("===================================")

while True:
    print("\nMenu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        with open("books.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([book_id, book_name, author, "Available"])

        print("Book added successfully!")

    elif choice == "2":
        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)

                print("\nLibrary Books")
                print("-------------------------------------------")

                for row in reader:
                    print("Book ID:", row[0])
                    print("Book Name:", row[1])
                    print("Author:", row[2])

                    if len(row) >= 4:
                        print("Status:", row[3])

                    if len(row) == 5:
                        print("Issued To:", row[4])

                    print("-------------------------------------------")

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

                        if len(row) >= 4:
                            print("Status:", row[3])

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

                        if len(row) >= 4:
                            status = row[3]
                        else:
                            status = "Available"

                        if len(row) == 5:
                            updated_rows.append([
                                update_id,
                                new_name,
                                new_author,
                                status,
                                row[4]
                            ])
                        else:
                            updated_rows.append([
                                update_id,
                                new_name,
                                new_author,
                                status
                            ])

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
        delete_id = input("Enter Book ID to delete: ")
        updated_rows = []
        found = False

        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row and row[0] == delete_id:
                        found = True
                    else:
                        updated_rows.append(row)

            with open("books.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if found:
                print("Book deleted successfully!")
            else:
                print("Book not found.")

        except FileNotFoundError:
            print("No books found.")

    elif choice == "6":
        issue_id = input("Enter Book ID to issue: ")
        student_name = input("Enter Student Name: ")

        updated_rows = []
        found = False

        try:
            with open("books.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row and row[0] == issue_id:
                        if len(row) >= 4 and row[3] == "Issued":
                            print("Book is already issued.")
                            updated_rows.append(row)
                        else:
                            updated_rows.append([
                                row[0],
                                row[1],
                                row[2],
                                "Issued",
                                student_name
                            ])
                            found = True
                    else:
                        updated_rows.append(row)

            with open("books.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)

            if found:
                print("Book issued successfully!")
            else:
                print("Book not found.")

        except FileNotFoundError:
            print("No books found.")
